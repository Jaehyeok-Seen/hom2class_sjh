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

'''
    1. 웹서비스를 만들건데, send 라고 하는 페이지를 보여주고 싶어.
    2. 그럼, 사용자는? send 페이지로 어떤 방식으로든 이동을 해야 함
    3. 그럼, 그 이동한 위치에 대한 처리는? URL을 관리하는 곳. 주소를 만들어 줘야함.

    1. 오늘부터 url을 관리하는 방법이 바꼈음.
    2. 왜 바꼈냐? 프로젝트에 app이 여러개가 되면... 조금 곤란할수도 있더라.
    3. articles app에서 하는 일을 실행시키려고 views.py를 불러오는 거랑
    4. posts app에서 하는 일을 실행시키려고, views.py를 불러오는 거랑 코드가 똑같다.
        from articles import views
        from posts import views as post_views
'''

from django.contrib import admin
# 각 앱이 할 일은 니들이 알아서 관리해라
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls'))
]
