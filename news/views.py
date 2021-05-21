from django.shortcuts import render
from .models import Post, PostCategory, Author, Category, Comment
from django.views.generic import ListView, DetailView

class news(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
