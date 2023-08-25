from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView


router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegisterView.as_view(), name='user-register'),            # 회원가입 Api 문서 Ok
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # 로그인 Api 문서 Ok
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),       # access token 리프레쉬 Api 문서 Ok

    path('get-random-money/', get_random_money, name='get-random-money')        # 1번 뷰
]