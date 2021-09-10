from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext_lazy as _
from django.http.response import Http404

from accounts.models import User

from .exceptions import IdMismatchError
from .forms import CommentForm, SubmitForm
from .models import Comment, Post


def index(request):
    return render(request, 'news/index.html', {
        'posts': Post.objects.all(),
    })


def search(request):
    search_term = request.GET.get('search_term', '')

    if search_term != '':
        posts = Post.get_posts_by_search_term(search_term=search_term)
    else:
        posts = []

    return render(request, 'news/search.html', {
        'posts': posts,
        'search_term': search_term,
    })


def by_author(request, username: str):
    try:
        user_data = User.get_by_username(username=username)
        posts = Post.get_posts_by_author(author=user_data)

        return render(request, 'news/by_author.html', {
            'posts': posts,
            'user_data': user_data,
        })
    except User.DoesNotExist:
        raise Http404


def comments(request, post_id: int):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)

        if form.is_valid():
            created_comment = form.save(commit=False)
            created_comment.author = request.user
            created_comment.post = post
            created_comment.save()

            messages.success(request, _('You\'ve successfully submitted your comment!'))

            return redirect('news:comments', post_id=post_id)
    else:
        form = CommentForm()

    return render(request, 'news/comments.html', {
        'comments': post.comment_set.filter(parent=None).all(),
        'form': form,
        'post': post,
    })


def reply(request, post_id: int, comment_id: int):
    try:
        comment = Comment.get_comment_by_id_and_post_id(comment_id=comment_id, post_id=post_id)

        if request.method == 'POST':
            form = CommentForm(request.POST)

            if form.is_valid():
                Comment.reply_to_comment(comment=comment, author=request.user, content=request.POST.get('content'))

                messages.success(request, _('You\'ve successfully replied to the comment!'))

                return redirect('news:comments', post_id=post_id)
        else:
            form = CommentForm()

        return render(request, 'news/reply.html', {
            'form': form,
            'comment': comment,
        })
    except IdMismatchError:
        raise Http404


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
