from pyexpat import model
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)  # 길이 제한 가능
    content = models.TextField()             # 길이 제한 불가
    created_at = models.DateTimeField()
    # author : 추후 작성 예정


    def __str__(self):
        return self.title