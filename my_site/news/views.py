from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext_lazy as _

from .forms import SubmitForm
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


@login_required
def create(request):
    if request.method == 'POST':
        form = SubmitForm(request.POST)

        if form.is_valid():
            created_item = form.save(commit=False)
            created_item.author = request.user
            created_item.save()

            messages.success(request, _('You\'ve successfully submitted a post!'))

            return redirect('news:index')
    else:
        form = SubmitForm()

    return render(request, 'news/create.html', {
        'form': form,
    })
