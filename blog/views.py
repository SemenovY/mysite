from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post


def post_list(request):
    """Создание представлений списка постов."""
    posts = Post.published.all()
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )


def post_detail(request, id):
    """Создание детальной информации о посте."""
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )
