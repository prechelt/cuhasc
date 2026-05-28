from django.urls import reverse

from cuhasc.models import Member, Team
import cuhasc.constants as c


class CuhascCookie:
    """Reads and writes the cuhasc browser cookie.

    Usage:
        cookie = CuhascCookie(request)
        cookie.add(team)
        response.set_cookie(COOKIE_NAME, cookie.cookietext)
    """

    SEP = '\t'

    def __init__(self, request):
        self._request = request
        self._entries = {}  # (modeltype_str, id) -> token
        self._parse(request.COOKIES.get(c.COOKIE_NAME, ''))

    def _parse(self, text):
        for line in text.splitlines():
            parts = line.strip().split(self.SEP)
            if len(parts) == 3:
                modeltype, id_str, token = parts
                try:
                    self._entries[(modeltype, int(id_str))] = token
                except ValueError:
                    pass

    def add(self, obj):
        """Add a Team or Member to the cookie."""
        self._entries[(type(obj).__name__, obj.id)] = obj.token

    @property
    def cookietext(self):
        """Serialize cookie as newline-separated 'modeltype;id;token' lines."""
        s = self.SEP
        return '\n'.join(f"{mt}{s}{id}{s}{tok}" for (mt, id), tok in self._entries.items())

    @property
    def teams(self):
        """List of Team objects stored in the cookie.

        Each Team has two extra properties added:
          url     -- relative URL of the team's edit_team page
          fullurl -- absolute URL (scheme + host + path) of the same page
        Requires the edit_team URL to be registered; raises NoReverseMatch until then.
        """
        result = []
        for (modeltype, obj_id), token in self._entries.items():
            if modeltype != 'Team':
                continue
            try:
                team = Team.objects.get(id=obj_id, token=token)
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
        for (modeltype, obj_id), token in self._entries.items():
            if modeltype != 'Member':
                continue
            try:
                member = Member.objects.get(id=obj_id, token=token)
            except Member.DoesNotExist:
                continue
            member.url = reverse('edit_member', args=[member.id, member.token])
            member.fullurl = self._request.build_absolute_uri(member.url)
            result.append(member)
        return result
