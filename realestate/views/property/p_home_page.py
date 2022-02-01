from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from realestate.models import Listing
from realestate.views import about_us
from realestate.views.property.choises import price_choices, bedroom_choices, state_choices


def property_listings(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    content = {
        'about_us': about_us(),
        'context': context,
        'header': {
            'title': 'Property Listing',
        }
    }

    return render(request, 'pages/property/listing/listing.html', context={'content': content})


def property_list_searching(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    content = {
        'about_us': about_us(),
        'header': {
            'title': 'Property Search',
        }
    }

    return render(request, 'listings/search.html', context={'content': content, 'context': context})
