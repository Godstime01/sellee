from allauth.account import views as allauth_views
from django.shortcuts import get_object_or_404
from .forms import AccountRegistrationForm

from .models import Referrals, USER


class AccountRegistionView(allauth_views.SignupView):
    form_class = AccountRegistrationForm


class ReferredAccountCreationView(allauth_views.SignupView):
    form_class = AccountRegistrationForm
    success_url = "user_dashboard"

    def get_referrer(self):
        """ """
        referrer_username = self.request.path.split("/")[-2]
        print(referrer_username)
        user = USER.objects.get(username=referrer_username)
        return user

    def form_valid(self, form):

        referrer = self.get_referrer()
        form = super().form_valid(form)
        print(self.user)
        referree = self.user
        print(referree, referrer)
        referrals = Referrals.objects.create(referrer=referrer, refferee=referree)
    
        referrals.save()
        return form
