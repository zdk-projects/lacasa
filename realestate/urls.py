from django.contrib import admin
from django.urls import path

from realestate.views.home_page import home_page, our_team, our_achievements, our_company

urlpatterns = [
    path('', home_page, name='home_page'),
    path('team', our_team, name='our_team'),
    path('achievements', our_achievements, name='our_achievements'),
    path('company', our_company, name='our_company'),
]
