from django.shortcuts import render

# Create your views here.
def index(request):
    # print(dir(request))
    # 내 articles의 메인 페이지를 보여주고싶어.
    # 근데 그 HTML을 그냥 보여주는게 아니라,
        # 우리가 진도를 나가면 뭔가 좀 더 특별한 무언가를 적어서
        # 완성된 HTML을 그려서 보여줄거야,
            # 전문용어로 렌더링 이라고 한다.
    # 그러면서 django에서 반드시 지켜야 할 약속이 무엇이냐.
    # 이런 HTML들은 반드시 app/templates/폴더 안에 넣어야 한다.
    return render(request, 'index.html')