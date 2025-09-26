## 🚀 AI 기반 여론 분석 기능 구현 리드미 (F05)

OpenAI의 LLM(거대 언어 모델)을 활용하여 
**수집된 종목별 댓글들의 전체적인 여론을 분석**하고 사용자에게 시각적으로 제공하는 기능을 구현했습니다.

===========================================================================================

## 1\. 개요 및 핵심 기능


| **기능명**   | AI 기반 댓글 여론 분석                                                                        |
| **목표**      | 특정 종목의 댓글들을 LLM으로 분석하여 4가지 카테고리(긍정, 부정, 중립, 정보공유)로 요약 제공. |
| **사용 기술** | **Python** (Django), **OpenAI API** (`gpt-5-nao`), **JavaScript** (Fetch API)               |
| **API 모델**  | `gpt-5-nano`                                                                                 |

===========================================================================================

## 2\. 백엔드 구현 (Django)

### 2.1. 분석 View (`crawlings/views.py`)

`analyze_sentiment` 함수를 추가하여 AI 분석 로직을 구현했습니다.

  - **OpenAI API 키 사용**: 보안을 위해 `os.getenv("OPENAI_API_KEY")`를 사용하여 **환경 변수**에서 API 키를 불러옵니다. **로컬 환경 설정 시 반드시 `OPENAI_API_KEY` 환경 변수를 등록해야 합니다.**
  - **데이터 필터링**: `company`와 `code`를 기반으로 해당 종목의 댓글 목록을 데이터베이스에서 조회합니다.
  - **프롬프트 엔지니어링**: LLM이 댓글 데이터를 정확하게 분석하고 요구된 JSON 형식으로 결과를 반환하도록 상세한 **시스템 메시지** 및 **사용자 프롬프트**를 구성했습니다.
  - **응답 형식**: 분석 결과는 프론트엔드에서 처리하기 쉽도록 **JSON** 형태로 반환됩니다.

<!-- end list -->

```python
# crawlings/views.py (주요 코드)
import os
from openai import OpenAI
# ... (다른 import)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_sentiment(request):
    # ... (댓글 조회 로직)

    # 프롬프트 구성 및 LLM 호출
    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[{"role": "system", "content": "당신은 금융 여론 분석 도우미입니다."},
                  {"role": "user", "content": prompt}], # prompt 변수에는 댓글과 형식 지정 내용 포함
        temperature=0.3,
    )
    # ... (결과 반환)
```

### 2.2. URL 경로 설정 (`crawlings/urls.py`)

새로 추가된 분석 함수에 접근할 수 있도록 URL 경로를 정의했습니다.

```python
# crawlings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ... (기존 경로)
    path('analyze/', views.analyze_sentiment, name='analyze'),  # F05 분석 경로
]
```

===========================================================================================

## 3 프론트엔드 구현 (HTML/JavaScript)

### 3.1. 템플릿 구조 및 스타일링 (`list.html`)

  - **분석 버튼**: 페이지 하단에 고정된 **'분석'** 버튼을 추가했습니다.
  - **결과 영역**: 분석 결과를 담을 `div` 영역(`id="analysis-result"`)을 추가했으며, 초기에는 숨겨져 있다가 분석 완료 시 나타나도록 설정했습니다.


### 3.2. JavaScript 로직 및 안정성 확보

버튼 클릭 시 백엔드 분석 API를 호출하고 결과를 표시하는 로직을 구현했습니다.


| **API 호출**           | `fetch` API를 사용하여 현재 페이지의 종목 정보(쿼리 파라미터)를 포함하여 `/crawlings/analyze/` 경로로 비동기 요청을 보냅니다.                                                                                                                                                      |
| **결과 처리**          | 응답으로 받은 JSON 결과(`data.result`)를 전처리 없이 `pre` 태그에 출력합니다.                                                                                                                                                                                                      |
| **렌더링 안정성 개선** | **오류 개선 사항**을 반영하여, 버튼 클릭 이벤트 리스너를 **`document.addEventListener("DOMContentLoaded", ...)`** 내부에 등록했습니다. 이는 **HTML DOM 트리가 완전히 로드된 후**에 스크립트가 실행되도록 보장하여, 버튼을 찾지 못해 클릭 이벤트가 동작하지 않는 문제를 해결합니다. |

```html
{% block content %}
    <div id="analysis-result" style="/* ... 스타일 ... */ display:none;">
      <h3>여론 분석 결과</h3>
      <pre id="analysis-text"></pre>
    </div>

    <button id="analyze-btn" style="/* ... 스타일 ... */">분석</button>

    <script>
    document.addEventListener("DOMContentLoaded", function() {
        // ... (클릭 이벤트 및 fetch 로직)
    });
    </script>
{% endblock content %}
```

===========================================================================================
## 4\. 환경 설정 및 디버깅 가이드

### 4.1. 필수 환경 변수

**AI 분석 기능을 사용하기 위해서는 로컬 환경 또는 배포 환경에 다음 환경 변수가 반드시 등록되어야 합니다.**

### 4.2. 디버깅 팁

  - **버튼 클릭 문제**: 버튼을 눌러도 아무 반응이 없다면, 브라우저 **개발자 도구 (F12) → Console 탭**을 확인하여 **`analyze-btn`** 요소를 찾지 못했다는 오류(`null` 오류)가 없는지 확인하세요. 이 경우 `list.html`에서 버튼과 JS가 **`{% block content %}`** 내부에 올바르게 위치했는지 재점검이 필요합니다.
  - **API 호출 문제**: 버튼 클릭 후 콘솔의 **Network 탭**에서 `/crawlings/analyze/` 요청이 \*\*실패(4xx, 5xx)\*\*했는지 확인합니다.
      - 400 Bad Request: 분석할 댓글이 없는 경우입니다.
      - 500 Internal Server Error: \*\*`OPENAI_API_KEY`\*\*가 잘못되었거나 설정되지 않은 경우, 또는 LLM 응답을 JSON으로 파싱하는 데 문제가 생긴 경우입니다.