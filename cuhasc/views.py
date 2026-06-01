from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed

from cuhasc.cookies import CuhascCookie
from cuhasc.forms import TeamForm
from cuhasc.models import Team
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
