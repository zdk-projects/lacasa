from django.urls import path, include

from realestate.views.home_page import home_page, our_team, our_achievements, our_company, contact_us, privacy_policy, \
    terms_and_conditions
from realestate.views.property.p_home_page import property_listings

from realestate.views.user.u_home_page import login_user, user_registration, dashboard, logout_user

urlpatterns = [
    path('', home_page, name='home_page'),
    path('team', our_team, name='our_team'),
    path('achievements', our_achievements, name='our_achievements'),
    path('company', our_company, name='our_company'),
    path('contact', contact_us, name='contact_us'),

    path('register_user', user_registration, name='user_registration'),
    path('login', login_user, name='login_user'),
    path('logout', logout_user, name='logout_user'),
    path('dashboard', dashboard, name='dashboard'),

    path('tos', terms_and_conditions, name='terms_and_conditions'),
    path('privacy-policy', privacy_policy, name='privacy_policy'),

    path('property-listings', property_listings, name='property_listings'),

]
