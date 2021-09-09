from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext_lazy as _
from django.http.response import Http404

from accounts.models import User

from .forms import CommentForm, SubmitForm
from .models import NewsItem


def index(request):
    search_term = request.GET.get('term', '')

    if search_term != '':
        news = NewsItem.get_news_items_by_search_term(search_term=search_term)
    else:
        news = NewsItem.objects.all()

    return render(request, 'news/index.html', {
        'news': news,
    })


def by_author(request, username: str):
    try:
        user_data = User.get_by_username(username=username)
        news = NewsItem.get_news_items_by_author(author=user_data)

        return render(request, 'news/by_author.html', {
            'news': news,
            'user_data': user_data,
        })
    except User.DoesNotExist:
        raise Http404


def comments(request, news_item_id):
    news_item = get_object_or_404(NewsItem, pk=news_item_id)

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)

        if form.is_valid():
            created_comment = form.save(commit=False)
            created_comment.author = request.user
            created_comment.news_item = news_item
            created_comment.save()

            messages.success(request, _('You\'ve successfully submitted your comment!'))

            return redirect('news:comments', news_item_id=news_item_id)
    else:
        form = CommentForm()

    return render(request, 'news/comments.html', {
        'comments': news_item.comment_set.filter(parent=None).all(),
        'form': form,
        'news_item': news_item,
    })


@login_required
def submit(request):
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

    return render(request, 'news/submit.html', {
        'form': form,
    })
