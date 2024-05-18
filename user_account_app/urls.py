from django.urls import path, include
from allauth.account import views as allauth_views
from . import views
from .forms import AccountLoginForm, AccountRegistrationForm

urlpatterns = [
    path(
        "login/",
        allauth_views.LoginView.as_view(form_class=AccountLoginForm),
        name="account_login",
    ),
    path(
        "register/<str:username>/",
        views.ReferredAccountCreationView.as_view(),
        name="account_signup",
    ),
    path("signup/", views.AccountRegistionView.as_view(), name="account_signup"),
    path("", include("allauth.urls")),
]
