from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from weights.models import Weight


# Create your views here.


@api_view(["GET"])
def get_weight_list(request):
    res_data = []

    Weight(id=1, weight_name="술찌", is_travel=False, amount=-2).save()
    Weight(id=2, weight_name="멸치", is_travel=False, amount=-2).save()
    Weight(id=3, weight_name="술고래", is_travel=False, amount=2).save()
    Weight(id=4, weight_name="돼지", is_travel=False, amount=2).save()
    Weight(id=5, weight_name="늦참", is_travel=False, amount=-2).save()
    Weight(id=6, weight_name="노잼", is_travel=False, amount=1).save()

    weights = Weight.objects.all()

    for weight in weights:
        data = {
            "weight_id": weight.pk,
            "weight_name": weight.weight_name,
        }
        res_data.append(data)

    return Response(data=res_data, status=status.HTTP_200_OK)
