from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all", views.all, name="all"),
    path("brend/<int:brend_id>", views.brend, name="brend"),
    path("type/<int:type_id>", views.type, name="type"),
    path("sex/<int:sex_id>", views.sex, name="sex"),
    path("resist/<int:resist_id>", views.resist, name="resist"),
    path("details/<int:Product_id>", views.details, name="details"),
    path("watchlist/<int:user_id>", views.watchlist, name="watchlist"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
