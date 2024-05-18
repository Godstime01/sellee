from django.contrib import admin

from .models import UserWallet, UserProfile

admin.site.register([UserWallet, UserProfile])