from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.utils.safestring import mark_safe

from cuhasc.cookies import CuhascCookie
from cuhasc.forms import MemberForm, QuestionnaireForm, TeamForm
import cuhasc.instruments as instruments
from cuhasc.models import Member, Team
import cuhasc.constants as c

DIMENSION_ORDER = ['PO', 'UN', 'CO', 'LT', 'MA']

_SVG_WIDTH = 500
_SVG_LEFT = 160   # space for dimension labels
_SVG_RIGHT = 20
_SVG_PLOT_W = _SVG_WIDTH - _SVG_LEFT - _SVG_RIGHT
_SVG_TOP = 20
_SVG_ROW_H = 50
_SVG_HEIGHT = _SVG_TOP + len(DIMENSION_ORDER) * _SVG_ROW_H + 20


def _score_to_x(score: float) -> float:
    return _SVG_LEFT + (score - 1) / 4 * _SVG_PLOT_W


def _culture_profile_svg(profile: dict[str, float], language: str) -> str:
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{_SVG_WIDTH}" height="{_SVG_HEIGHT}">',
    ]
    # axis tick marks and labels at 1..5
    for score in range(1, 6):
        x = _score_to_x(score)
        lines.append(
            f'<line x1="{x}" y1="{_SVG_TOP - 5}" x2="{x}" y2="{_SVG_TOP + len(DIMENSION_ORDER) * _SVG_ROW_H}"'
            f' stroke="#ccc" stroke-width="1"/>'
        )
        lines.append(
            f'<text x="{x}" y="{_SVG_TOP - 8}" text-anchor="middle" font-size="11" fill="#888">{score}</text>'
        )
    # one row per dimension
    for i, code in enumerate(DIMENSION_ORDER):
        y = _SVG_TOP + i * _SVG_ROW_H + _SVG_ROW_H // 2
        label = instruments.get_dimension_name(code, language)
        # horizontal line
        lines.append(
            f'<line x1="{_SVG_LEFT}" y1="{y}" x2="{_SVG_WIDTH - _SVG_RIGHT}" y2="{y}"'
            f' stroke="#aaa" stroke-width="1"/>'
        )
        # label to the left
        lines.append(
            f'<text x="{_SVG_LEFT - 8}" y="{y + 4}" text-anchor="end" font-size="12" fill="#333">{label}</text>'
        )
        # dot if score defined
        if code in profile:
            x = _score_to_x(profile[code])
            lines.append(
                f'<circle cx="{x:.1f}" cy="{y}" r="8" fill="#0d6efd"/>'
            )
    lines.append('</svg>')
    return '\n'.join(lines)


def home(request):
    cookie = CuhascCookie(request)
    return render(request, "cuhasc/home.html", {
        'teams': cookie.teams,
        'members': cookie.members,
    })


def create_team(request):
    if request.method == 'GET':
        form = TeamForm()
        return render(request, "cuhasc/create_team.html", {'form': form})
    elif request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save()
            cookie = CuhascCookie(request)
            cookie.add(team)
            response = redirect('show_team', id=team.id, token=team.token)
            response.set_cookie(c.COOKIE_NAME, cookie.cookietext)
            return response
        return render(request, "cuhasc/create_team.html", {'form': form})
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


def show_team(request, id, token):
    team = get_object_or_404(Team, id=id, token=token)
    return render(request, "cuhasc/show_team.html", {'team': team})


def edit_team(request, id, token):
    team = get_object_or_404(Team, id=id, token=token)
    if request.method == 'GET':
        form = TeamForm(instance=team)
        return render(request, "cuhasc/edit_team.html", {'form': form, 'team': team})
    elif request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('show_team', id=team.id, token=team.token)
        return render(request, "cuhasc/edit_team.html", {'form': form, 'team': team})
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


def create_member(request, team_id, member_token):
    team = get_object_or_404(Team, id=team_id, member_token=member_token)
    if request.method == 'GET':
        form = MemberForm()
        qform = QuestionnaireForm(instruments.get_questionnaire('en'), instruments.get_scales('en'))
        return render(request, "cuhasc/create_member.html",
                      {'form': form, 'qform': qform, 'team': team})
    elif request.method == 'POST':
        form = MemberForm(request.POST)
        qform = QuestionnaireForm(instruments.get_questionnaire('en'), instruments.get_scales('en'), request.POST)
        if form.is_valid() and qform.is_valid():
            member = form.save(commit=False)
            member.team = team
            member.save()
            qform.save_results(member)
            cookie = CuhascCookie(request)
            cookie.add(member)
            response = redirect('show_member', id=member.id, token=member.token)
            response.set_cookie(c.COOKIE_NAME, cookie.cookietext)
            return response
        return render(request, "cuhasc/create_member.html",
                      {'form': form, 'qform': qform, 'team': team})
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


def show_member(request, id, token):
    member = get_object_or_404(Member, id=id, token=token)
    cookie = CuhascCookie(request)
    language = cookie.get_language() or 'en'
    profile = member.culture_profile()
    svg = mark_safe(_culture_profile_svg(profile, language)) if profile else None
    return render(request, "cuhasc/show_member.html", {
        'member': member,
        'culture_profile_svg': svg,
    })


def edit_member(request, id, token):
    member = get_object_or_404(Member, id=id, token=token)
    if request.method == 'GET':
        form = MemberForm(instance=member)
        existing = {qr.item: str(qr.value) for qr in member.qresults.all()}
        qform = QuestionnaireForm(instruments.get_questionnaire('en'), instruments.get_scales('en'), initial=existing)
        return render(request, "cuhasc/edit_member.html",
                      {'form': form, 'qform': qform, 'member': member})
    elif request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        qform = QuestionnaireForm(instruments.get_questionnaire('en'), instruments.get_scales('en'), request.POST)
        if form.is_valid() and qform.is_valid():
            form.save()
            qform.save_results(member)
            return redirect('show_member', id=member.id, token=member.token)
        return render(request, "cuhasc/edit_member.html",
                      {'form': form, 'qform': qform, 'member': member})
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
