from django.db import models
# 자 django는 과연 User Model을 어디에 뒀을까.
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 다른 모든 앱들과 유일하게 차이가 나는 부분은
# User 모델을 정의 하기 위해 필요한 부모 클래스의 이름이 다르다.
    # 왜 다를까?
    # 기존의 다른 모델들은 그냥, Model을 정의 하기 위한 기능만 가져오면 된다.
    # 반면에, User는 이미 django가 가지고 있었던 User 모델을 상속 받아야 하니까
        # 상속 받을 부모 클래스의 위치와 종류가 다르다.
class User(AbstractUser):
    pass