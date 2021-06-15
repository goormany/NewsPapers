from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from .filters import newsFilter
from .forms import NewsForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class news(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = '-data'
    paginate_by = 5


class new(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Post
    template_name = 'new_home.html'
    context_object_name = 'new'
    permission_required = 'news.view_post'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['com_post'] = Comment.objects.filter(commentPost=self.kwargs['pk']).values("commentText")
        context['pc_post'] = PostCategory.objects.filter(pcPost=self.kwargs['pk']).values("pcCategory")
        return context

class newSearch(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Post
    template_name = 'new_search.html'
    context_object_name = 'newsearch'
    ordering = '-data'
    permission_required = 'news.view_post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = newsFilter(self.request.GET, queryset=self.get_queryset())
        return context

class newsCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    template_name = 'news/news_add.html'
    form_class = NewsForm
    permission_required = 'news.add_post'

class newsDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'news/news_delete.html'
    queryset = Post.objects.all()
    context_object_name = 'newd'
    success_url = '/news/'
    permission_required = 'news.delete_post'

class newsUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Post
    template_name = 'news/news_update.html'
    form_class = NewsForm
    permission_required = 'news.change_post'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class CategoryDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Category
    template_name = 'category/category_detail.html'
    permission_required = 'news.view_category'
    context_object_name = 'categores'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context





