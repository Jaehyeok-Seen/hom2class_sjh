from django.shortcuts import render

# Create your views here.
def send(request):
    # 하는 일
    # 파이썬의 함수가 하는 일은 항상 무언가를 return 하는것
    # html을 반환 하는것 (웹 사이트니까)
        # 이쁘게 잘 그려서 반환
    # 우리는 django와 약속했다. 뭘?
        # 내가 반환해야할 html 파일은 (template)
        # 모두 app/templates/ 라는 폴더에 모아 두기로
    # return 'send.html'
    return render(request, 'send.html')

# django가 첫번째 인자를 항상 requests를 받는 이유가 뭐다?
# 사용자가 보낸 요청과 관련된 모든 정보를 이 view함수에서 넘겨주기 위해서
def receive(request):
    # 어떤 요청이 오면 그 요청에 "맞는" 응답을 하는게 이 함수가 하는 일
    # print(request)
    # print(dir(request))
    # print(request.GET)
    message = request.GET.get('message')
    # HTML파일에 python이 가진 변수에 있는 값을 넘겨서 보여줘야 한다고?
    # 원래는 그런게 가능할 리가 없다! HTML은 프로그래밍 언어가 아니다.
        # render야 너가 receive.html 그릴때, 내가 가진 message 변수의 어떤 값도 같이 보여주면 안될까?
        # 내가 html은 그렇게 만들어 놓을게
    # map(int, input().split())
    context = {
        'message': message
    }
    return render(request, 'receive.html', context)

def profile(request, username):
    # 함수의 매개변수를 잘 정의해 준다.
    # 무언가 엄청난 일
        # 무언가 대단한 코드
    # 뭔가 복잡한 일
    context = {
        'username': username
    }
    return render(request, 'profile.html', context)