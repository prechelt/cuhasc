from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create_team", views.create_team, name="create_team"),
    path("show_team/<int:id>/<str:token>", views.show_team, name="show_team"),
]
