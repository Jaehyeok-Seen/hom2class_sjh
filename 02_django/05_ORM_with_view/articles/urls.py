from django.urls import path
from . import views
'''
# 이름을 지어주자
# 왜? 
    # 내가 나중에 편할려고
    # url이 엄청 길어져
    # /articles/{article_pk}/comments/{comment_pk}/edit/
        # 이런것들을 a태그나 form태그에서 손으로 쓰고 있다고 생각해 보십쇼.
        # 농담으로 똑같은거 여러번 쓰기 싫다고 하긴 했는데
        # 정확하게는 오타가 날 확률을 줄인다
    # articles:comment_edit
'''

app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
]
