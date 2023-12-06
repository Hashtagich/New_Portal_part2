from django.views.generic import ListView, DetailView
from .models import Post


class PostsList(ListView):
    model = Post
    ordering = '-datetime_post'
    template_name = 'posts.html'
    context_object_name = 'news'


class PostsList2(ListView):
    model = Post
    ordering = '-datetime_post'
    template_name = 'posts_ver2.html'
    context_object_name = 'news'


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'news'
