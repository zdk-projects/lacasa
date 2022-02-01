from django.shortcuts import render
from realestate.models import Team, Achievement, HomeListing
from . import about_us


# Create your views here.
def home_page(request):
    listings = HomeListing.objects.order_by('-list_date').filter(is_published=True)[:10]

    content = {
        'about_us': about_us(),
        'listing': listings,
        'nbar': 'home',
    }
    return render(request, 'pages/home/index.html', context={'content': content})


def our_team(request):
    team_members = {
        'mvp': [],
        'team': [],

    }
    for members in Team.objects.all():
        if members.is_mvp:
            team_members['mvp'].append({
                'name': members.name,
                'position': members.position,
                'message': members.message,
                'image': members.photo_1,
            })
        else:
            team_members['team'].append({
                'name': members.name,
                'position': members.position,
                'location': members.city,
                'image': members.photo_1,
            })
        print(team_members)

    content = {
        'about_us': about_us(),
        'team': team_members,
        'nbar': 'home',
        'header': {
            'title': 'Our Team',
        }
    }
    return render(request, 'pages/home/team.html', context={'content': content})


def our_achievements(request):
    achievements = Achievement.objects.all().order_by('-id')
    content = {
        'about_us': about_us(),
        'nbar': 'home',
        'achievements': achievements,
        'header': {
            'title': 'Over Achievements',
        }
    }
    return render(request, 'pages/home/achievements.html', context={'content': content})


def our_company(request):
    content = {
        'about_us': about_us(),
        'nbar': 'home',
        'header': {
            'title': 'Our Company',
        }
    }
    return render(request, 'pages/home/company.html', context={'content': content})


def contact_us(request):
    content = {
        'about_us': about_us(),
        'nbar': 'contact_us',
        'header': {
            'title': 'Contact Us',
        }
    }
    return render(request, 'pages/contact/contact_us.html', context={'content': content})


def privacy_policy(request):
    content = {
        'about_us': about_us(),
        'header': {
            'title': 'Privacy Policy',
        }
    }
    return render(request, 'pages/privacy-policy/index.html', context={'content': content})


def terms_and_conditions(request):
    content = {
        'about_us': about_us(),
        'header': {
            'title': 'Terms and Conditions',
        }
    }
    return render(request, 'pages/privacy-policy/term-and-services.html', context={'content': content})
