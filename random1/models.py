from django.db import models
from django.contrib.auth.models import  AbstractUser

# 커스티마이징 한 User
class User(AbstractUser):
    nickname = models.CharField(max_length=30, unique=True) # 사용자의 닉네임 validators=[validate_unique_nickname]
    
