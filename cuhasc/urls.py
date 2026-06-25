from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create_team", views.create_team, name="create_team"),
    path("show_team/<int:id>/<str:token>", views.show_team, name="show_team"),
    path("edit_team/<int:id>/<str:token>", views.edit_team, name="edit_team"),
    path("create_member/<int:team_id>/<str:member_token>", views.create_member, name="create_member"),
    path("show_member/<int:id>/<str:token>", views.show_member, name="show_member"),
    path("edit_member/<int:id>/<str:token>", views.edit_member, name="edit_member"),
    path("adminpage/<str:token>", views.adminpage, name="adminpage"),
]
