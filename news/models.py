from django.db import models
from django.utils.text import Truncator

from accounts.models import User

from .exceptions import IdMismatchError


class NewsItem(models.Model):
    title = models.CharField(max_length=256)
    url = models.URLField(max_length=2000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    @staticmethod
    def get_news_items_by_author(author: User):
        return NewsItem.objects.filter(author=author)

    @staticmethod
    def get_news_items_by_search_term(search_term: str):
        return NewsItem.objects.filter(title__icontains=search_term)

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

    @staticmethod
    def get_comment_by_id_and_news_item_id(comment_id: int, news_item_id: int):
        comment = Comment.objects.get(pk=comment_id)

        if comment.news_item.id != news_item_id:
            raise IdMismatchError()

        return comment

    @staticmethod
    def reply_to_comment(comment, author: User, content: str):
        return comment.comment_set.create(news_item=comment.news_item, author=author, content=content)

    def has_replies(self):
        return self.comment_set.count() > 0

    def get_replies(self):
        return self.comment_set.filter(parent=self).all()
