from django.views.generic import View
from django.shortcuts import render, redirect

from .models import Post, Tag
from .utils import ObjectDetailsMixin, ObjectCreateMixin
from .forms import PostForm, TagForm


class PostDetails(ObjectDetailsMixin, View):
    model = Post
    template = 'blog/post_details.html'


class TagDetails(ObjectDetailsMixin, View):
    model = Tag
    template = 'blog/tag_details.html'


class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})
