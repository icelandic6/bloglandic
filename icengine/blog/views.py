from django.shortcuts import render

from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


def post_details(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_details.html', context={'post': post})
