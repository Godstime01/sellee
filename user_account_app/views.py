from allauth.account import views as allauth_views
from .forms import AccountRegistrationForm
from .models import Referrals, UserProfile
from .utils import generate_user_referral_link
from django.dispatch import Signal


class AccountRegistionView(allauth_views.SignupView):
    
    def form_valid(self, form):
        # Create a custom signal class and signal to create user profile 

        return super().form_valid(form)

class ReferredAccountCreationView(allauth_views.SignupView):
    form_class = AccountRegistrationForm
    success_url = 'login'

    def form_valid(self, form):
        form = super().form_valid(form)

        referree = form.username
        referrer = self.request.path[-2]  # tp get the username in the request path

        referrals = Referrals.objects.create(referrer=referrer, referree=referree)

        referrals.save()

        # create a refferal
        return form
    

