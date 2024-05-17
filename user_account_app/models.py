from django.db import models
from django.contrib.auth import get_user_model

USER = get_user_model()


# Create your models here.
class Referrals(models.Model):
    referrer = models.ForeignKey(USER, related_name='referrer', on_delete=models.CASCADE)
    refferee = models.ForeignKey(USER, related_name='referree', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def calculate_referral_bonus(self):
        """The referral bonus would be given when the refferee makes a purchase"""
        pass


class UserWallet(models.Model):
    user = models.OneToOneField(USER, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=16, decimal_places=2, default = 0)


class UserBillingInformation(models.Model):
    pass


class UserProfile(models.Model):
    image = models.ImageField(upload_to='profile_image/', default='user_profile.png')
    user = models.OneToOneField(USER, on_delete=models.CASCADE)
    
    def __str__(self): self.user.username