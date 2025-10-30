from django.urls import path
from . import views


app_name = 'reservations'

urlpatterns = [
    path('', views.index, name='index'),
    # 앞에 이미 http://127.0.0.1:8000/reservations/ 가 작성되어 있고
    # 그 뒤에 뭐라고 요청이오면 처리할 경로를 지정하는 것
    # 1. 사용자가 어떤 경로로 요청을 보내면
    # 2. 그때 실행할 함수를 지정해 주고
    # 3. 그 경로에 이름을 붙여주자.
    path('create/', views.create, name='create')
]