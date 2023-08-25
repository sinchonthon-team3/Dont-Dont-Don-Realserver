from django.contrib import admin
from django.urls import path

from travel.views import get_distribution_view


app_name='travel'
urlpatterns = [
    path('', get_distribution_view),
]