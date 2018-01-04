# -*- coding: utf8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from Household_Management.api.views import get_init_data, get_search_data, add_insert_data, migrate, get_card_init_data, get_card_search_data, add_card_data

urlpatterns = [
    # Examples:
    # url(r'^$', 'Household_Management.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^get_init_data/$', get_init_data),
    url(r'^get_search_data/$', get_search_data),
    url(r'^add_insert_data/$', add_insert_data),
    url(r'^migrate/$', migrate),
    url(r'^get_card_init_data/$', get_card_init_data),
    url(r'^get_card_search_data/$', get_card_search_data),
    url(r'^add_card_data/$', add_card_data),
]
