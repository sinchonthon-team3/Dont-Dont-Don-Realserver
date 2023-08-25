from django.urls import path, include

from weights.views import get_weight_list

urlpatterns = [
    path('', get_weight_list),
]
