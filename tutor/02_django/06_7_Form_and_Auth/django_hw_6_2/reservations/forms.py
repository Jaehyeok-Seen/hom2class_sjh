from django import forms
from .models import Reservation


# 예약을 위한 form 태그를 구성할 클래스
    # 모델에 대한 정보를 가진 클래스
    # 아, 이거 이름 어떻게 외웁니까?
        # 모델에 대한 정보를 가진 form
    # 주관식으로 나오면 철자 틀릴거 같은데요?
        # pep-8에서 정한 우리끼리의 약속
        # 전세계 모든 파이썬 개발자는 클래스명
        # PascalCase로 적음
class ReservationForm(forms.ModelForm):
    '''
    원래 Form이라는 클래스는 무엇을 위한것이냐
    진짜 말 그대로 form태그를 어떻게 구성할것인가를
    내가 직접 하나하나 만들수 있는 툴을 제공하는것
        그건, Model이 없을때에 대한 이야기.
    form 태그에서 보여줘야할 label, input 태그가 어떻게 생겼을지 여기서 정할 수 있어야함.
    title = forms.TextField()
    '''
    
    # Meta Data: 이 데이터를 위한 데이터
    # Meta Class: 이 클래스를 위한 클래스
    class Meta: # 이 form은 예약을 위한 form태그를 어떻게 구성할건지를 정의하는 것이다.
        # 그럼 이 ModelForm을 위한 Meta 클래스는 어떤 정보를 가지면 좋을까?
        # 1. 어떤 모델을 토대로 form 태그를 만들 것이냐
        model = Reservation
        # 2. form 태그를 구성할때, 어떤 필드들 (사용자가 입력해야 할 공간)을 어떻게 구성할 것이냐.
            # 필드들 -> 복수형
        fields = '__all__'  # 전부다.
            # 우리가 아직 파이썬에 안익숙하가보니 겪게되는 아쉬운점.
            # 사실 저 표기 방식도 전세계 모든 파이썬 유저는 다 알고 있는 표현임
            # 매직 메서드 __str__, __repr__, __len__, 등등...
        