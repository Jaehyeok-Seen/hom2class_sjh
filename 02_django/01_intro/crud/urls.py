"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 이런 경로로 요청이 들어오면 뭘 할건데?
    # 사용자에게 그 메인 페이지의 모습을 보여 줘야 한다.
        # 인터넷 페이지는? HTML로 작성함.
        # 그 HTML을 사용자에게 `반환` 해야함. -> return
        # 그걸 파이썬으로 만들어야함.           -> function
        # view 함수라고 부른다.
    path('articles/', views.index),  # index라는 함수를 views.py에서 가져와서 쓴다.
]
'''
def path(route, view, kwargs=None, name=None):
    Response = view(사용자의 요청 정보)
'''
