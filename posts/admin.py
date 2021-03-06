from django.contrib import admin
from django.utils.text import Truncator

from .models import Comment, Post


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'number_of_replies', 'show_post')

    @staticmethod
    def number_of_replies(obj: Comment):
        return obj.comment_set.count()

    @staticmethod
    def show_post(obj: Comment):
        return Truncator(obj.post.title).chars(32)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'author', 'created_at')


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
