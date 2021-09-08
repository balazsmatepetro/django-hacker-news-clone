from django.shortcuts import get_object_or_404, render

from .models import NewsItem


def index(request):
    search_term = request.GET.get('term', '')

    if search_term != '':
        news = NewsItem.get_news_items_by_term(search_term=search_term)
    else:
        news = NewsItem.objects.all()

    return render(request, 'news/index.html', {
        'news': news,
    })


def comments(request, news_item_id):
    news_item = get_object_or_404(NewsItem, pk=news_item_id)

    return render(request, 'news/comments.html', {
        'comments': news_item.comment_set.filter(parent=None).all(),
        'news_item': news_item,
    })
