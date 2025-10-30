from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 게시글이 생성 되는 시점: 자동으로 지금 (추가 될 때)
    created_at = models.DateTimeField(auto_now_add=True)
    # 게시글이 수정 된 시점: 자동으로 지금
    updated_at = models.DateTimeField(auto_now=True)