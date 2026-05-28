from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create_team", views.create_team, name="create_team"),
]
