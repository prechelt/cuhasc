from django.db import models

import cuhasc.base as base
import cuhasc.constants as c


def init_member_token() -> str:
    return base.random_token(c.TOKEN_LENGTH_MEMBER)


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


class Member(models.Model):
    name = models.CharField(max_length=100)
    token = models.CharField(max_length=c.TOKEN_LENGTH_MEMBER)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = base.random_token(c.TOKEN_LENGTH_MEMBER)
        super().save(*args, **kwargs)


