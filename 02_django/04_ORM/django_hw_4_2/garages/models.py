from django.db import models
# from django.db.models import TextField, IntegerField, BooleanField

# Create your models here.
'''
Django를 통해서 우리가 기대하는바가 무엇인가?
0. 기획: 무슨 서비스를 만들 것이냐?
    - 지금은 주차장 관리 서비스를 만들 것이다.
        - 그럼 무슨 데이터를 다룰 것이냐?
        - 주차장에 대한 정보를 다룰 것이다.
1. Web 서비스를 만드는 것 (이 서비스에서 다뤄야할 데이터는 애초에 정해져있었지않을까?)
    - 그 Web 서비스를 위해서는 어떤 것들이 필요한가?
    - 어디로? 갔을때? 볼 수 있을까? (URL)
        - 어떤? 정보를 가지고 올지를 정하는 함수 (View)
            - 사용자가 볼 수 있는 페이지에 넣을 데이터 (Model)
                - 사용자가 볼 수 있을 어떤 페이지 (HTML)
'''

'''
    models.py 라는 파일에
    class로 주차장에 대한 정보를 정의한 이유?
    - 우리는 파이썬 문법 밖에 몰라요!
        - 하지만, 주차장에 대한 정보가 필요해요!
        - 그래서, 그 정보로 view함수에서 잘 써서
            - 사용자가 요청한 `서울` 주차장에 대한 정보를
            - HTML로 그려서 사용자에게 넘겨 줘야 해요.

    그럼 ORM 이라는 친구는 왜 필요한가?
        - 그건 어디까지나 우리가 파이썬 문법만 써서 편하게 쓰고 싶지만
        - data라는건 결국 여러가지 이유로 (자세한 이유는 DB 수업시간에)
            그런 data는 RDBMS 이라는걸 통해서 SQL라는 문법으로 다루는게 맞다.
        근데 그렇다고 해서 여전히 내가 파이썬 문법밖에 모른다 라는 사실이 달라지나?
            (언젠간 달라질거임 SQL 배울거거든)
        - 나는 빨리 그냥 파이썬으로 웹 서비스 만들고 싶다고!!!

    예시) 미국에 놀러갔어요.
    - 나는 한국어 밖에 몰라.
    - 근데 식당에서 빨리 음식 주문하고 싶어!!
        - 번역기 키는거죠.
        - 나는 그냥 한국어라 말하면 
            - 번역기가 영어로 번역 해줌
        - 상대방도 그냥 영어로 말하면
            - 번역기가 한글로 번역 해줌
    - ORM -> django가 다 만들어 놨다.

    저희 왜 django 배워요? 
        1. 한국은 Spring 많이 쓴다는데
            - 그럼 Java 배우시든지
            - 그래도 취업하려면 Java가 좋다던데? Spring이 좋다던데?
            - 파이썬을 배우고, Django를 배운뒤에 
                Java와 Spring을 공부하는건 지금 드는 노력의 1/10이면 됨.
        2. Web 개발자 안할건데 django 왜 배움?
            - Web 개발 과정에서 기본적인 프로그래밍과 데이터의 흐름을 이해해라
            - 지금 우리가 네트워크의 통신 방식을 깊게 들어가지않음
                - 그냥 가장 기본적인 `요청` 과 `응답`을 처리하는 방법을 배우는것
'''

'''
    class는 왜 만드나?
    공통된 속성을 가진 어떠한 개체들을 하나의 class로 묶어서 관리하면 편하다.
    class person:
        blood_color = 'red'

    p1 = Person()
    p2 = Person()
    p1.blood_color == p2.blood_color

    # p2가 외계인에게 납치당했어. 그래서 어떤 인체실험을 당해
    p2.blood_color = 'blue' 로 바꾸면?

'''
# 파이썬에서만 쓸 수 있는 방법임
    # DB 라는곳에 똑같은 모양이 되도록 잘 만들수 있도록 어떤 과정을 거쳐야함.
    # DB라는 곳에서는 반드시 지켜야만 하는 규칙이 있는데
        # PRIMARY KEY 라고 부르는 고유한 식별자 (주민등록증) 같은걸 만들어 줘야함
class Garage(models.Model):
    # 클래스 속성 (공통 속성)
        # 자, 아래에 있는 각 속성들에 저장 할 수 있는 타입을 지정 해 줄게~
    # ctrl + alt + 방향키 위 아래 (커서가 늘어남)
    # ctrl + 방향키 좌 우 (단어 별 이동)
    location = models.TextField()   # location에는 글자만 저장되어야 한다.
    capacity = models.IntegerField() # capacity는 정수만 저장되어야 한다.
    is_parking_available = models.BooleanField() # Boolean만 저장되어야 한다.
    opening_time = models.TimeField() # 시간 정보만 저장되어야 한다.
    closing_time = models.TimeField() # 시간 정보만 저장되어야 한다.
    price = models.IntegerField()   # 가격 정보를 추가했다.

# 데이터를 저장할 수 있는 공간 마련을 모두 끝났다.
'''
    1. python으로 데이터 생김새와 특성 정의하기
    2. 그걸 DB에 옮길 수 있도록 명세서 만들기 (makemigrations)
    3. 실제 DB에다가 그 명세서대로 table 만들기 (migrate)
'''

# 그 DB라는 곳에 진짜 데이터를 삽입(Create), 조회(Read), 수정(Update), 삭제(Delete)
    # CRUD 라는걸 해 보자.
    # 어케하는데? 여전히 나는 파이썬 밖에 모름!
'''
    class Person:
        blood_color = 'red'

    p1 = Person()
    p1.blood_color = 'blue' <- 이런식으로 인스턴스 속성 정의...하는게 가능은했는데...
    p1.save()
'''

서울 = Garage()
서울.location = '서울'
서울.capacity = 30
서울.is_parking_available = False
서울.opening_time = "07:00"
서울.closing_time = "23:00"
서울.price = 3000
# 여기까지는 뭐다? 파이썬 문법일 뿐이다.
    # 계속 생각하자. 파이썬 문법 다음에 할 일!!!!
    # DB에게도 알려주기
# 데이터 베이스에 저장하기 라는 메서드
서울.save()


부산 = Garage()
# ctrl + D => 내가 드래그한 글자랑 똑같은 글자 모두 선택
부산.location = '부산'
부산.capacity = 20
부산.is_parking_available = True
부산.opening_time = "08:00"
부산.closing_time = "22:00"
부산.price = 2000
부산.save()

# 주차장 정보좀 한번 다 봅시다. (request)
'''주차장 전체 정보를 보여주는 함수 (View)
    # 그럼.. 주차장 전체 정보를 가져와서
    # HTML에 그려서
    # 사용자에게 반환
'''

# Garage이 클래스로 어떻게 잘 하면 데이터를 볼 수 있지않을까?
# Garage이 클래스로 만든 instance로 데이터 저장도 했는데.

# 우리는 Garage 클래스에게 전체 주차장 정보를 달라고 요청   (함수 호출)
    # DB야 Garage가 가진 `모든` 객체 나한테 주라.
# 클래스야, 너가 가진 `모든` `객체` 정보 내놔
# objects manager의 역할은
    # all 전체 조회나
    # filter 어떤 조건 검색이나
    # get 엄격한 조건 검색이나 기타 등등을 수행하는
# QuerySet API를 가지고 있는 어떤 객체
# 주차장이가진.객체들(데이터들).중에전부()
garages = Garage.objects.all()    # ORM
# 여러개를 가져왔는데 -> 아마 list 같이 생긴 곳에 있곘지?
    # 걔네들이 가진 모든 내용을 다 출력 해보고 싶어
    # [<서울 object>, <부산 object> ... ]
for garage in garages:
    print(garage.location)
# 주차장이가진.객체들(데이터들).특정조건을 만족하는것 하나(pk=1)
garage = Garage.objects.get(pk=1)
# 주차장이가진.객체들(데이터들).중에 특정 조건을 만족하는 애들(location='서울')
garages = Garage.objects.filter(location='서울')

# 수정??? 
# 1. 누구를 수정할건데
garage = Garage.objects.get(pk=2)
# 2. 뭘 수정할건데
    # 원래는 garage.location에 들어있던 값은 '부산'
    # 그걸 내가 location 변수에 들어있느 값을 '구미'로 바꾼거
'''
    dust = 60
    dust = 50
    print(dust) # 50
'''
garage.location = '구미'
# 3. 수정해서 어따 쓸건데?
# DB에 반영해야지 -> 저장 해야지
garage.save()

# 삭제
# 1. 누구 삭제 할건데
garage = Garage.objects.get(pk=1)
# 2. 뭐할건데
garage.delete()