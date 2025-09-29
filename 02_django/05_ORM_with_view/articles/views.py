from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # 여기서 할 일 html을 보여준다.
    articles = Article.objects.all()
    # print(articles)
    # for article in articles:
    #     print(article.title)
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        # print(request.POST)
        # 처음으로 게시글 페이지로 요청이 오면 우리가 할 일은?
        # 게시글 생성 페이지를 반환 해 주기
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:index')
    # 함수는 return 하면 코드가 종료 되서 밑에 코드가 안보이네 뭐가 이상하네?
    # 아...POST랑 GET이랑 따로 처리해야지!
    return render(request, 'create.html')