from django.shortcuts import render

from .models import NewsItem


def index(request):
    latest_news = NewsItem.objects.order_by('-created_at').all()

    return render(request, 'news/index.html', {
        'news': latest_news,
    })
