from django.urls import path, include
from django.conf.urls.static import url
from .views import *
urlpatterns = [
    path('oauth/', include('social_django.urls', namespace='social')),
]