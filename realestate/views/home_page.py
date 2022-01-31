from django.shortcuts import render
from realestate.models import AboutUs
from . import about_us


# Create your views here.
def home_page(request):
    content = {
        'about_us': about_us()
    }
    return render(request, 'pages/home/index.html', context={'content': content})


def our_team(request):
    content = {
        'about_us': about_us()
    }
    return render(request, 'pages/home/team.html', context={'content': content})


def our_achievements(request):
    content = {
        'about_us': about_us()
    }
    return render(request, 'pages/home/achievements.html', context={'content': content})


def our_company(request):
    content = {
        'about_us': about_us()
    }
    return render(request, 'pages/home/company.html', context={'content': content})


def contact_us(request):
    content = {
        'about_us': about_us()
    }
    return render(request, 'pages/contact/contact_us.html', context={'content': content})


def privacy_policy(request):
    content = {
        'about_us': about_us()
    }
    return render(request, 'pages/privacy-policy/index.html', context={'content': content})


def terms_and_conditions(request):
    content = {
        'about_us': about_us()
    }
    return render(request, 'pages/privacy-policy/term-and-services.html', context={'content': content})
