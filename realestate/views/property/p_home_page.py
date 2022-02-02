from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from realestate.models import HouseListing
from realestate.views import about_us
from realestate.views.property.choises import price_choices, bedroom_choices, state_choices


def house_listing(request):
    listings = HouseListing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 8)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    content = {
        'about_us': about_us(),
        'context': context,
        'nbar': 'house_listing',
        'header': {
            'title': 'Houses Listing',
        }
    }

    return render(request, 'pages/property/listing/listing.html', context={'content': content})


def house_details(request, slug):
    listing = get_object_or_404(HouseListing, slug=slug)

    context = {
        'listing': listing
    }
    content = {
        'about_us': about_us(),
        'context': context,
        'nbar': 'house_listing',
        'header': {
            'title': 'Houses Listing',
        }
    }

    return render(request, 'pages/property/listing/home_listing.html', content)


def house_listing_search(request):
    queryset_list = HouseListing.objects.order_by('-list_date')

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
        'nbar': 'house_listing',
        'header': {
            'title': 'Property Search',
        }
    }

    return render(request, 'listings/search.html', context={'content': content, 'context': context})
