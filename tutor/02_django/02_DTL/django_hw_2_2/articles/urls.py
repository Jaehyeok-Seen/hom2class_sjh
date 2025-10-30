from django.urls import path
from . import views
# from articles import views

# dust = 50
# dust = 60

# 이제 이름을 붙이자.
app_name = 'articles'

# send 라는 경로로 요청이 오면?
urlpatterns = [
    path('send/', views.send, name='send'),
    path('receive/', views.receive, name='receive'),
    # SNS를 만들었다고 가정
        # 유저 수 만큼 path를 만들어? 말도 안된다.
    # path('dlwlrma/', views.profile, name='profile'),
    # path('rokmnd_official/', views.profile, name='profile'),
    # path('????/', views.profile, name='profile'),
    # path('또 다른 유저/', views.profile, name='profile'),
    # path('새로운 유저/', views.profile, name='profile'),

    # 다 똑같이 동작할 건데, 어떤 값 하나만 바꾸면 됨.
        # -> 이거 할려고 우리는 뭘 만들었을까?
        # TC가 10갠데, 10개 전부다 똑같은 코드가 실행되어야 한다.
        # 근데 TC가 10개일때, 입력값은 다 다르다.
        # 그래서 우리는 for 문 안에서 무언가를 호출했다.
            #
    # path함수의 첫번째 인자에 들어갈 값만 어떻게 바뀌게 하면 될 듯?
        # 그럼.. 사용자가 입력한 어떤 값을 그대로 쓰는게 아니라,
        # 어떤 변수에 담아서 쓰면 될 듯?
    path('<username>/', views.profile, name='profile')
    # 질문. 경로에 적은 변수명 username은 왜 profile view함수 만들때
        # 정의한 매개변수랑 이름이 같아야 할까?
]

'''
def BFS(n):
    pass

T = int(input())
for tc in range(1, T+1):
    N = int(input)
    # 이제 이 N마다 서로 다른 BFS 함수 호출
    BFS(N)

    print(f'#{tc} {result}')

'''