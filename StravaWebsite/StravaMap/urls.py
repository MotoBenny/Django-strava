from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', base_map, name='Base Map View'),
    path('connected/', connected_map, name='Connect Map view'),
    path('oauth/', include("social_django.urls", namespace="social")),
]