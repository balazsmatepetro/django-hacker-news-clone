from django.shortcuts import get_object_or_404, render

from .models import NewsItem


def index(request):
    latest_news = NewsItem.objects.order_by('-created_at').all()

    return render(request, 'news/index.html', {
        'news': latest_news,
    })


def comments(request, news_item_id):
    news_item = get_object_or_404(NewsItem, pk=news_item_id)

    return render(request, 'news/comments.html', {
        'comments': news_item.comment_set.filter(parent=None).all(),
        'news_item': news_item,
    })
