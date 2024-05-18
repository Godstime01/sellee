from typing import Any
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CardCreationForm, CoinCreationForm
from .models import Card, Coin

from user_account_app import models


class DashboardOverview(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"


class DashboardAllCards(LoginRequiredMixin, ListView):
    model = Card
    template_name = "dashboard/cards.html"
    context_object_name = "cards"


class DashboardCreateCard(LoginRequiredMixin, CreateView):
    template_name = "dashboard/create_card.html"
    form_class = CardCreationForm
    success_url = "/dashboard/cards"


class DashboardAllCoin(LoginRequiredMixin, ListView):
    model = Coin
    template_name = "dashboard/coins.html"
    context_object_name = "coins"


class DashboardCreateCoin(LoginRequiredMixin, CreateView):
    template_name = "dashboard/create_coin.html"
    form_class = CoinCreationForm
    success_url = "/dashboard/coins"


class DashboardUserWallet(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/user_wallet.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        user_wallet_info = models.UserWallet.objects.get(user=self.request.user)
        print(user_wallet_info)

        context_data = super().get_context_data(**kwargs)
        context_data["wallet_info"] = user_wallet_info
        return context_data


class DashboardUserReferalView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/user_referral.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        user_profile = models.UserProfile.objects.get(user=self.request.user)

        context_data = super().get_context_data(**kwargs)

        context_data["referral_link"] = user_profile.unique_referral_link
        return context_data
