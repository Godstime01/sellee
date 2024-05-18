from django.contrib.sites.shortcuts import get_current_site


def generate_user_referral_link(request, user):
    domain =  get_current_site().domain
    print(domain)
    return f'{domain}{user.username}'