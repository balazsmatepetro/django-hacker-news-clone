from django.contrib import admin

from .models import NewsItem


class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'author', 'created_at')


admin.site.register(NewsItem, NewsItemAdmin)
