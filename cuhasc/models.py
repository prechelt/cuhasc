from collections import defaultdict

from django.db import models

import cuhasc.base as base
import cuhasc.constants as c


def init_member_token() -> str:
    return base.random_token(c.TOKEN_LENGTH_MEMBER)


class AdminPage(models.Model):
    """Singleton holding the token for the admin page, via which a Culture Lead can
    recover the Team and Member links if the cookie is lost. Created and re-tokened by
    the ``cuhasc-adminpage`` management command; only one instance ever exists."""
    token = models.CharField(max_length=c.TOKEN_LENGTH_ADMINPAGE)


class Team(models.Model):
    name = models.CharField(max_length=100)
    token = models.CharField(max_length=c.TOKEN_LENGTH_TEAM)
    member_token = models.CharField(max_length=c.TOKEN_LENGTH_MEMBER,
                                    default=init_member_token)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = base.random_token(c.TOKEN_LENGTH_TEAM)
            self.member_token = base.random_token(c.TOKEN_LENGTH_MEMBER)
        super().save(*args, **kwargs)

    def culture_profile(self) -> dict:
        """Team Culture Profile: each Member's Culture Profile plus the per-Dimension
        team mean Score. A Member with zero answers has no Culture Profile and is
        omitted from both the member list and the aggregate."""
        members: list[dict] = []
        for member in self.members.all():
            profile = member.culture_profile()
            if profile:
                members.append({'name': member.name, 'profile': profile})
        means: dict[str, float] = {}
        dimensions = {dim for m in members for dim in m['profile']}
        for dim in dimensions:
            scores = [m['profile'][dim] for m in members if dim in m['profile']]
            means[dim] = sum(scores) / len(scores)
        return {'members': members, 'means': means}


class Member(models.Model):
    name = models.CharField(max_length=100)
    token = models.CharField(max_length=c.TOKEN_LENGTH_MEMBER)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = base.random_token(c.TOKEN_LENGTH_MEMBER)
        super().save(*args, **kwargs)

    def culture_profile(self) -> dict[str, float]:
        answers: dict[str, list[int]] = defaultdict(list)
        for qr in self.qresults.all():
            dimension = qr.item.rstrip('0123456789')
            answers[dimension].append(qr.value)
        return {dim: sum(vals) / len(vals) for dim, vals in answers.items()}


class QResult(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='qresults')
    item = models.CharField(max_length=20)
    scale = models.CharField(max_length=50)
    value = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = [('member', 'item')]


