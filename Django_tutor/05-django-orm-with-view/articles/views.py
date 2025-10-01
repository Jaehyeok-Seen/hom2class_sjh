from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

# --- Read ---
def index(request):
    """전체 게시글 목록을 조회하여 index.html 페이지를 렌더링"""
    # 1. Article 모델을 통해 DB에 저장된 모든 데이터를 조회
    articles = Article.objects.all()

    # 2. 조회된 데이터를 템플릿에 전달하기 위해 context 딕셔너리에 담음
    #    템플릿에서는 'articles'라는 키로 QuerySet 객체에 접근할 수 있음
    context = {
        'article': articles,
    }
    # 3. request, 템플릿 경로, context를 render 함수에 전달하여 최종 HTML을 생성하고 사용자에게 응답
    return render(request, 'articles/index.html', context)

# 게시글 상세 페이지를 응답하는 함수 
#(어떤 일을 해야하는가?)
# 1. 몇번 게시글인지를 DB에 조회
# 2. 조회한 상세 게시글 데이터를 템플릿과 함께 응답
def detail(request, pk): # detail은 변수가 하나 더 들어옴, variable routing, 이 pk는 urls의 <int:pk>와 일치해야함
    # 1. 단일 게시글 조회 ( queryset API method 중 get())
    
    # Article.objects.get(id=pk) 같다
# def detail(request,article_pk):
#     Article.objects.get(pk = article_pk) 앞에 urls에 가서도 다 바꿔줘야함
    article = Article.objects.get(pk=pk) #이때 pk혼동 주의 ( 오른쪽 pk가 위 매개변수에 담긴 인자),(왼쪽 pk는 article column을 의미)

    # 2. 단일 게시글 데이터와 템플릿을 응답
    context = {
        'article' : article, #받을려면 담아줘야한다. 
    }
    return render(request, 'articles/detail.html', context)

# 사용자가 게시글 생성을 위한 작성 페이지를 응답하는 함수
def new(request):
    return render(request, 'articles/new.html')

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Article.objects.create(title=title, content=content)
        return redirect('articles:index')
    else:
        return redirect('articles:new')