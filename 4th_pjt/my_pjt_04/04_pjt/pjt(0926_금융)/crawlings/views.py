# crawlings/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST
from django.urls import reverse
from .models import Comment
from .services import fetch_toss_comments
import os
from django.http import JsonResponse
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@require_http_methods(["GET"])
def index(request):
    return render(request, "crawlings/index.html")

@require_http_methods(["POST"])
def fetch(request):
    company = request.POST.get("company_name", "").strip()
    if not company:
        return render(request, "crawlings/index.html", {"error": "회사명을 입력하세요."})
    try:
        code, comments = fetch_toss_comments(company, limit=30, max_scroll=12)
    except Exception as e:
        return render(request, "crawlings/index.html", {"error": f"크롤링 실패: {e}"})

    Comment.objects.bulk_create(
        [Comment(company_name=company, stock_code=code, content=c) for c in comments],
        ignore_conflicts=True
    )
    # ✅ 리스트 화면에 회사명/코드 표시를 위해 쿼리스트링으로 전달
    list_url = f"{reverse('crawlings:list')}?company={company}&code={code}"
    return redirect(list_url)

@require_http_methods(["GET"])
def comment_list(request):
    qs = Comment.objects.order_by("-id")
    # 쿼리스트링 우선, 없으면 최신 댓글의 회사/코드로 대체
    company = request.GET.get("company")
    code = request.GET.get("code")
    if not (company and code) and qs.exists():
        latest = qs.first()
        company = company or latest.company_name
        code = code or latest.stock_code
    ctx = {"comments": qs, "company": company, "code": code}
    return render(request, "crawlings/list.html", ctx)

@require_POST
def delete_comment(request, pk):
    get_object_or_404(Comment, pk=pk).delete()
    # 삭제 후 현재 회사/코드 유지
    company = request.GET.get("company", "")
    code = request.GET.get("code", "")
    base = reverse("crawlings:list")
    sep = "&" if ("?" in base) else "?"
    return redirect(f"{base}?company={company}&code={code}")


def analyze_sentiment(request):
    """댓글 전체 여론 분석"""
    company = request.GET.get("company", "")
    code = request.GET.get("code", "")

    comments = Comment.objects.filter(company_name=company, stock_code=code).values_list("content", flat=True)
    if not comments:
        return JsonResponse({"error": "분석할 댓글이 없습니다."}, status=400)

    # 프롬프트 구성
    prompt = f"""
    아래는 {company}({code}) 종목에 대한 댓글들입니다.
    각 댓글을 참고하여 전체적인 여론을 4가지 카테고리로 요약해주세요:
    - 긍정
    - 부정
    - 중립
    - 정보공유

    결과는 JSON 형식으로:
    {{
      "긍정": "요약 내용",
      "부정": "요약 내용",
      "중립": "요약 내용",
      "정보공유": "요약 내용"
    }}
    댓글들:
    {list(comments)}
    """

    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[{"role": "system", "content": "당신은 금융 여론 분석 도우미입니다."},
                  {"role": "user", "content": prompt}],

    )

    content = response.choices[0].message.content.strip()
    return JsonResponse({"result": content})