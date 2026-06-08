from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed

from cuhasc.cookies import CuhascCookie
from cuhasc.forms import MemberForm, QuestionnaireForm, TeamForm
import cuhasc.instruments as instruments
from cuhasc.models import Member, Team
import cuhasc.constants as c


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
    return render(request, "cuhasc/show_member.html", {'member': member})


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
