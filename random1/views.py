from .models import *

from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserRegisterSerializer

from rest_framework.decorators import api_view, permission_classes
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions, status
from rest_framework.response import Response

from random import *
import math

User = get_user_model()

# 회원가입
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    
# 로그인
class CustomTokenObtainPairView(TokenObtainPairView):
    pass  

###################### view 만들기 ######################

# 1. total금액을 randomly 할당해서 보내주기
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def get_random_money(request):
    
    participants = request.data.get('participants') # 사람들 목록 받아오기 (리스트)
    total_cost = request.data.get('total_cost')   # 총 금액

    # 클라이언트로부터 값이 안 왔을 때 예외처리
    if not participants or not total_cost:
        return Response({"error": "participants or total_cost is missing"}, status=status.HTTP_404_NOT_FOUND)
    
    parti_len = len(participants) 
    random_index_list = []
    sum = 0

    # 0 ~ 20 이렇게 설정해놓고 난수 뽑아서 각자 인덱스에 넣어주기!
    for i in range(parti_len):
        temp = randint(0, 20)
        random_index_list.append(temp)
        sum += temp

    total_list = []
    for i in range(parti_len):
        cost = math.ceil(total_cost * (random_index_list[i] / sum))
        percent = (random_index_list[i] / sum) * 100
        total_list.append([cost, round(percent, 1)])  # [가격, 퍼센트] 


    final_result = {}  # map으로
    final_result["normal"] = math.ceil(total_cost / parti_len)
    for i in range(parti_len):
        final_result[participants[i]] = total_list[i]

    # 클라이언트에게 결과 보내주기
    return Response(final_result, status=status.HTTP_200_OK)


