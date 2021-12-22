"""Define URL-s for users app"""
from django.urls import path, include

from . import views

app_name = "users"
urlpatterns = [
    #login
    path('',include('django.contrib.auth.urls')),
    #register
    path('register/',views.register, name='register'),
]
