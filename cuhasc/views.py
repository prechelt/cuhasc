import markdown
from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse, Http404, HttpResponseNotAllowed
from django.utils.safestring import mark_safe

import cuhasc.constants as c
import cuhasc.handbook as handbook
import cuhasc.i18n as i18n
import cuhasc.instruments as instruments
from cuhasc.cookies import CuhascCookie
from cuhasc.forms import MemberForm, QuestionnaireForm, TeamForm
from cuhasc.models import AdminPage, Member, Team
from cuhasc.plots import culture_profile_svg, team_culture_profile_svg


def _resolve_language(cookie) -> str:
    """Questionnaire language for the initial render: cookie choice if still available,
    else English. (HTTP Accept-Language detection is out of scope, see ADR-0002.)"""
    lang = cookie.get_language()
    return lang if lang in instruments.get_languages() else 'en'


def _selector_context(language: str) -> dict:
    """Template context for the questionnaire language selector."""
    return {
        'languages': i18n.language_options(instruments.get_languages()),
        'current_language': i18n.language_options([language])[0],
    }


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
    cookie = CuhascCookie(request)
    language = cookie.get_language() or 'en'
    team_profile = team.culture_profile()
    svg = (mark_safe(team_culture_profile_svg(team_profile, language))
           if team_profile['members'] else None)
    return render(request, "cuhasc/show_team.html", {
        'team': team,
        'team_culture_profile_svg': svg,
    })


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
    cookie = CuhascCookie(request)
    if request.method == 'GET':
        language = _resolve_language(cookie)
        form = MemberForm()
        qform = QuestionnaireForm(instruments.get_questionnaire(language),
                                  instruments.get_scales(language))
        return render(request, "cuhasc/create_member.html",
                      {'form': form, 'qform': qform, 'team': team, **_selector_context(language)})
    elif request.method == 'POST':
        switch = request.POST.get('switch_language')
        if switch is not None:
            language = switch if switch in instruments.get_languages() else 'en'
            cookie.set_language(language)
            form = MemberForm(initial={'name': request.POST.get('name', '')})
            qform = QuestionnaireForm(instruments.get_questionnaire(language),
                                      instruments.get_scales(language),
                                      initial=request.POST.dict())
            response = render(request, "cuhasc/create_member.html",
                              {'form': form, 'qform': qform, 'team': team,
                               **_selector_context(language)})
            response.set_cookie(c.COOKIE_NAME, cookie.cookietext)
            return response
        language = _resolve_language(cookie)
        form = MemberForm(request.POST)
        qform = QuestionnaireForm(instruments.get_questionnaire(language),
                                  instruments.get_scales(language), request.POST)
        if form.is_valid() and qform.is_valid():
            member = form.save(commit=False)
            member.team = team
            member.save()
            qform.save_results(member)
            cookie.add(member)
            response = redirect('show_member', id=member.id, token=member.token)
            response.set_cookie(c.COOKIE_NAME, cookie.cookietext)
            return response
        return render(request, "cuhasc/create_member.html",
                      {'form': form, 'qform': qform, 'team': team, **_selector_context(language)})
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


def show_member(request, id, token):
    member = get_object_or_404(Member, id=id, token=token)
    cookie = CuhascCookie(request)
    language = cookie.get_language() or 'en'
    profile = member.culture_profile()
    svg = mark_safe(culture_profile_svg(profile, language)) if profile else None
    return render(request, "cuhasc/show_member.html", {'member': member, 'culture_profile_svg': svg})


def adminpage(request, token):
    get_object_or_404(AdminPage, token=token)
    teams = Team.objects.prefetch_related('members').all()
    return render(request, "cuhasc/adminpage.html", {'teams': teams})


def handbook_section(request, slug):
    section = handbook.get_section_by_slug(slug)
    if section is None:
        raise Http404
    body_html = mark_safe(markdown.markdown(section.body))
    return render(request, "cuhasc/handbook_section.html",
                  {'section': section, 'body_html': body_html})


def handbook_image(request, filename):
    if '/' in filename or filename in ('.', '..'):
        raise Http404
    path = c.IMAGE_POOL_DIR / filename
    if not path.is_file():
        raise Http404
    return FileResponse(path.open('rb'))


def edit_member(request, id, token):
    member = get_object_or_404(Member, id=id, token=token)
    cookie = CuhascCookie(request)
    if request.method == 'GET':
        language = _resolve_language(cookie)
        form = MemberForm(instance=member)
        existing = {qr.item: str(qr.value) for qr in member.qresults.all()}
        qform = QuestionnaireForm(instruments.get_questionnaire(language),
                                  instruments.get_scales(language), initial=existing)
        return render(request, "cuhasc/edit_member.html",
                      {'form': form, 'qform': qform, 'member': member, **_selector_context(language)})
    elif request.method == 'POST':
        switch = request.POST.get('switch_language')
        if switch is not None:
            language = switch if switch in instruments.get_languages() else 'en'
            cookie.set_language(language)
            form = MemberForm(initial={'name': request.POST.get('name', member.name)})
            qform = QuestionnaireForm(instruments.get_questionnaire(language),
                                      instruments.get_scales(language),
                                      initial=request.POST.dict())
            response = render(request, "cuhasc/edit_member.html",
                              {'form': form, 'qform': qform, 'member': member,
                               **_selector_context(language)})
            response.set_cookie(c.COOKIE_NAME, cookie.cookietext)
            return response
        language = _resolve_language(cookie)
        form = MemberForm(request.POST, instance=member)
        qform = QuestionnaireForm(instruments.get_questionnaire(language),
                                  instruments.get_scales(language), request.POST)
        if form.is_valid() and qform.is_valid():
            form.save()
            qform.save_results(member)
            return redirect('show_member', id=member.id, token=member.token)
        return render(request, "cuhasc/edit_member.html",
                      {'form': form, 'qform': qform, 'member': member, **_selector_context(language)})
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
