from django.contrib.auth.models import User
from django.db import models
from django.utils.text import Truncator


class NewsItem(models.Model):
    title = models.CharField(max_length=256)
    url = models.URLField(max_length=2000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} ({Truncator(text=self.url).chars(num=64)})'

