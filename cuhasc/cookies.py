from dataclasses import dataclass, asdict
import json

from django.urls import reverse

from cuhasc.models import Member, Team
import cuhasc.constants as c


@dataclass
class Role:
    classname: str
    id: int
    token: str


class CuhascCookie:
    """Reads and writes the cuhasc browser cookie.

    Usage:
        cookie = CuhascCookie(request)
        cookie.add(team)
        response.set_cookie(COOKIE_NAME, cookie.cookietext)
    """

    def __init__(self, request):
        self._request = request
        self._roles: dict[tuple[str, int], Role] = {}
        self._language: str | None = None
        self._parse(request.COOKIES.get(c.COOKIE_NAME, ''))

    def _parse(self, text):
        if not text:
            return
        try:
            data = json.loads(text)
        except (json.JSONDecodeError, TypeError):
            return
        for entry in data.get('roles', []):
            try:
                role = Role(classname=entry['classname'], id=int(entry['id']), token=entry['token'])
                self._roles[(role.classname, role.id)] = role
            except (KeyError, ValueError):
                pass
        lang = data.get('language')
        if isinstance(lang, str):
            self._language = lang

    def add(self, obj):
        """Add a Team or Member to the cookie."""
        role = Role(classname=type(obj).__name__, id=obj.id, token=obj.token)
        self._roles[(role.classname, role.id)] = role

    def set_language(self, lang: str):
        self._language = lang

    def get_language(self) -> str | None:
        return self._language

    @property
    def cookietext(self) -> str:
        data: dict = {'roles': [asdict(r) for r in self._roles.values()]}
        if self._language is not None:
            data['language'] = self._language
        return json.dumps(data)

    @property
    def teams(self):
        """List of Team objects stored in the cookie.

        Each Team has two extra properties added:
          url     -- relative URL of the team's edit_team page
          fullurl -- absolute URL (scheme + host + path) of the same page
        Requires the edit_team URL to be registered; raises NoReverseMatch until then.
        """
        result = []
        for role in self._roles.values():
            if role.classname != 'Team':
                continue
            try:
                team = Team.objects.get(id=role.id, token=role.token)
            except Team.DoesNotExist:
                continue
            team.url = reverse('edit_team', args=[team.id, team.token])
            team.fullurl = self._request.build_absolute_uri(team.url)
            result.append(team)
        return result

    @property
    def members(self):
        """List of Member objects stored in the cookie.

        Each Member has two extra properties added:
          url     -- relative URL of the member's edit_member page
          fullurl -- absolute URL (scheme + host + path) of the same page
        Requires the edit_member URL to be registered; raises NoReverseMatch until then.
        """
        result = []
        for role in self._roles.values():
            if role.classname != 'Member':
                continue
            try:
                member = Member.objects.get(id=role.id, token=role.token)
            except Member.DoesNotExist:
                continue
            member.url = reverse('edit_member', args=[member.id, member.token])
            member.fullurl = self._request.build_absolute_uri(member.url)
            result.append(member)
        return result
