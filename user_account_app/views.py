from allauth.account import views as allauth_views
from .forms import AccountRegistrationForm
from .models import Referrals



class AccountRegistionView(allauth_views.SignupView):
    form_class = AccountRegistrationForm
    

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
    

