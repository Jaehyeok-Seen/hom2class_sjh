from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm

# Create your views here.
def index(request):
    # 전체 예약 정보를 ORM을 통해 조회 한뒤 변수에 담았고
    reservations = Reservation.objects.all()
    # 그 변수에 들어있을 데이터들을 딕셔너리에 담은뒤
    context = {
        'reservations': reservations
    }
    # 사용자의 요청에 따라서 전체 예약 목록을 보여주는 HTML을 그리는구나.
    return render(request, 'reservations/index.html', context)

def create(request):
    # print(dir(request))
    # print(request.method)
    '''주의
        제발 부탁이니 코드 외워서 쓰지 마십쇼.
        create 함수처럼 
        게시글 생성 페이지와
        게시글 생성 처리 기능 2가지를 한곳에서 처리하려고 할 때,
        많은 분들이 처음부터 그 2가지 기능의 코드를 다 작성하고 넘어가려고 합니다.
        왜? 외웠으니까.
    '''
    # 만약 create view함수가 POST 방식의 요청에 응답한다면
    if request.method == 'POST': 
        # 데이터를 생성 해 달라는 요청이 왔다는 것!
        # 생성 하고 싶은 데이터는? request에 POST에 들어있곘지 (정상적인 방법이었다면)
        reservation_form = ReservationForm(request.POST)
        # 이제 사용자가 넘긴 데이터를 토대로, DB에 넣어도 될까? 체크
        if reservation_form.is_valid(): # 유효성 검사
            reservation_form.save()     # 여기까지 create 함수가 해 줘야하는 일\
            # 그건 우리 개발자들끼리는 그렇게 생각하는데.. 우리 서비스 쓰는 유저는 그렇지 않음
            # 아... 게시글 생성 됐으면, 생성 됐는지 보여 달라고!!! 이뭐 나보고 어쩌라고?
                # 난 요청 하나에 대한 처리 끝났으니, UX를 위해서 다른 부서로 보내자
                # 그 완성된 데이터 유저님 보여드려라.
            return redirect('reservations:index')
        
    # 포스트가 아닐때는?
    else:
        '''
        # 가장 먼저 우리가 이 view함수 왜 만들었는지 생각해 보면
        # 별다른거 없이 그냥 예약 생성 페이지를 보여달라고 했을때, 실행될 함수로써 적기 시작했다.

        # create.html을 그릴때, 그냥 그리는게 아니라 내가만든
        # ModelForm을 사용해서 Form을 좀 편하고 이쁘게 그려줭
        '''
        reservation_form = ReservationForm()
    context = {
        'reservation_form': reservation_form
    }
    return render(request, 'reservations/create.html', context)
