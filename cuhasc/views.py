from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed

from cuhasc.forms import TeamForm


def home(request):
    return render(request, "cuhasc/home.html")


def team_create(request):
    if request.method == 'GET':
        form = TeamForm()
        return render(request, "cuhasc/team_create.html", {'form': form})
    elif request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, "cuhasc/team_create.html", {'form': form})
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])
