from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'sampleapp'
urlpatterns = [
    path('detail/<id>', detail, name='detail'),
    path('home/', home, name='home'),
    path('profile/<id>', profile, name='profile'),
    path('ml', mlrocks)
]
