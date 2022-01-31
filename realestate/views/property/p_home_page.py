from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from realestate.models import Contact
from realestate.views import about_us


def property_listings(request):
    content = {
        'about_us': about_us()
    }

    return render(request, 'pages/property/listing/listing.html', context={'content': content})
