from django.conf import settings
from django.db import models
from django.utils import timezone

#пост в блоге
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#автор поста
    title = models.CharField(max_length=200)#название поста
    text = models.TextField()#текст поста
    created_date = models.DateTimeField(default=timezone.now)#дата создания
    published_date = models.DateTimeField(blank=True, null=True)#дата публикации
    #публикация
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    #Ввозвращает заголовок поста
    def __str__(self):
        return self.title
