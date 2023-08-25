import math

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from weights.models import Weight

User = get_user_model()

# Create your views here.


@api_view(["POST"])
def get_distribution_view(request):
    Weight(id=1, weight_name="술찌", is_travel=False, amount=-2).save()
    Weight(id=2, weight_name="멸치", is_travel=False, amount=-2).save()
    Weight(id=3, weight_name="술고래", is_travel=False, amount=2).save()
    Weight(id=4, weight_name="돼지", is_travel=False, amount=2).save()
    Weight(id=5, weight_name="늦참", is_travel=False, amount=-2).save()
    Weight(id=6, weight_name="노잼", is_travel=False, amount=1).save()
    req_data = request.data.copy()
    req_user_datas = req_data.pop("user")
    total_price = req_data.get("total_price")
    member_count = len(req_user_datas)
    print(member_count)
    total_amount = 0
    user_amount_list = []
    user = []
    for data in req_user_datas:
        print(data)
        user_amount = 10
        weight_ids = data.pop("weight_ids")
        for weight_id in weight_ids:
            weight = Weight.objects.get(id=weight_id)
            user_amount += weight.amount
        user_amount_list.append(user_amount)
        total_amount += user_amount

    cnt = 0
    for user_amount in user_amount_list:
        percentage = user_amount/total_amount
        user_pay = math.ceil(total_price * percentage)
        user_data = {
            "name": req_user_datas[cnt].get("name"),
            "percentage": round(percentage*100, 1),
            "change_pay": user_pay,
        }
        cnt += 1
        user.append(user_data)
    res_data = {
        'user': user,
        'default_pay': math.ceil(total_price / member_count)
    }

    return Response(data=res_data, status=status.HTTP_200_OK)
