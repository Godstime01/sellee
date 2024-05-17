from django.urls import path, include
from allauth.account import views as allauth_views
from . import views
from .forms import AccountLoginForm, AccountRegistrationForm

urlpatterns = [
    path("login/", allauth_views.LoginView.as_view(form_class = AccountLoginForm), name = 'account_login'),
    path("signup/<str:username>/", views.ReferredAccountCreationView.as_view(), name = 'account_signup'),
    path("signup/", allauth_views.SignupView.as_view(form_class = AccountRegistrationForm), name = 'account_signup'),
    path('', include('allauth.urls')),
]