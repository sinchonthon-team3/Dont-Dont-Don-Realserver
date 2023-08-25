from django.contrib import admin
from django.urls import path

from friends.views import get_distribution_view

urlpatterns = [
    path('get-distribution-view/', get_distribution_view),
]