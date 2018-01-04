from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from Household_Management.api import urls as api_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'Household_Management.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api_urls)),
    url(r'^accounts/login/$', auth_views.login),
]
