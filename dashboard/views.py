from django.views.generic import TemplateView, View, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CardCreationForm, CoinCreationForm
from .models import Card, Coin


class DashboardOverview(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"


class DashboardAllCards(ListView):
    model = Card
    template_name = "dashboard/cards.html"
    context_object_name = 'cards'


class DashboardCreateCard(CreateView):
    template_name = "dashboard/create_card.html"
    form_class = CardCreationForm
    success_url = "/dashboard/cards"


class DashboardAllCoin(ListView):
    model = Coin
    template_name = "dashboard/coins.html"
    context_object_name = 'coins'


class DashboardCreateCoin(CreateView):
    template_name = "dashboard/create_coin.html"
    form_class = CoinCreationForm
    success_url = "/dashboard/coins"