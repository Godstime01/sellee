from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('wallet/', views.DashboardUserWallet.as_view(), name = 'user_wallet'),
    path('referral/', views.DashboardUserReferalView.as_view(), name = 'referral_view'),
    path(
        "users/",
        TemplateView.as_view(template_name="dashboard/users.html"),
        name="dashboard_user",
    ),
    path("cards/", views.DashboardAllCards.as_view(), name="dashboard_list_cards"),
    path(
        "cards/create/",
        views.DashboardCreateCard.as_view(),
        name="dashboard_create_card",
    ),
    path("coin/", views.DashboardAllCoin.as_view(), name="dashboard_list_coins"),
    path(
        "coin/create/",
        views.DashboardCreateCoin.as_view(),
        name="dashboard_create_coin",
    ),
    path("", views.DashboardOverview.as_view(), name="user_dashboard"),
]
