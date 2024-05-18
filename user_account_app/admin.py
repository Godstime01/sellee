from django.contrib import admin

from .models import UserWallet, UserProfile, Referrals

admin.site.register([UserWallet, UserProfile, Referrals])