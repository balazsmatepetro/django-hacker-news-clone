from django.contrib.auth.models import User
from django.db import models
from django.utils.text import Truncator


class NewsItem(models.Model):
    title = models.CharField(max_length=256)
    url = models.URLField(max_length=2000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_news_items_by_term(search_term: str):
        return NewsItem.objects.order_by('-created_at').filter(title__icontains=search_term)

    def get_number_of_comments(self):
        return self.comment_set.count()

    def __str__(self):
        return f'{self.title} ({Truncator(text=self.url).chars(num=64)})'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    news_item = models.ForeignKey(NewsItem, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def has_replies(self):
        return self.comment_set.count() > 0

    def get_replies(self):
        return self.comment_set.filter(parent=self).all()
