from django.contrib import admin
from django.utils.text import Truncator

from .models import Comment, NewsItem


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'number_of_replies', 'show_news_item')

    @staticmethod
    def number_of_replies(obj: Comment):
        return obj.comment_set.count()

    @staticmethod
    def show_news_item(obj: Comment):
        return Truncator(obj.news_item.title).chars(32)


class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'author', 'created_at')


admin.site.register(Comment, CommentAdmin)
admin.site.register(NewsItem, NewsItemAdmin)