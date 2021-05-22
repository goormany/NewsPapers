from django.shortcuts import render
from .models import Post, PostCategory, Author, Category, Comment
from django.views.generic import ListView, DetailView
from datetime import datetime

class news(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-data')


class new(DetailView):
    model = Post
    template_name = 'new_home.html'
    context_object_name = 'new'
