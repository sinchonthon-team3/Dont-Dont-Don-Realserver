import math

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from weights.models import Weight


User = get_user_model()


@api_view(["POST"])
def get_distribution_view(request):
    
    Weight(id=1, weight_name="운전자", is_travel=True, amount=-2).save()
    Weight(id=2, weight_name="예약자", is_travel=True, amount=-1).save()
    Weight(id=3, weight_name="선발대", is_travel=True, amount=-1).save()
    Weight(id=4, weight_name="장보기", is_travel=True, amount=-2).save()
    Weight(id=5, weight_name="설거지", is_travel=True, amount=-1).save()
    Weight(id=6, weight_name="뒷정리", is_travel=True, amount=-1).save()
    Weight(id=7, weight_name="노잼", is_travel=True, amount=-1).save()
    Weight(id=8, weight_name="꿀잼", is_travel=True, amount=1).save()
    Weight(id=9, weight_name="대노잼", is_travel=True, amount=-2).save()
    Weight(id=10, weight_name="대꿀잼", is_travel=True, amount=2).save()
    
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
            "default_pay": math.ceil(total_price/member_count)
        }
        cnt += 1
        user.append(user_data)

    return Response(data=user, status=status.HTTP_200_OK)