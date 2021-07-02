from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.core.paginator import Paginator
from .filters import newsFilter
from .forms import NewsForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from .tasks import hello


class news(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'

    # paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cate'] = Category.objects.all()
        return context

    def get_queryset(self):
        return Post.objects.filter(public=True).order_by('-data')


    def get(self, request):
        hello.delay()
        return HttpResponse('Hello!')


class new(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Post
    template_name = 'new_home.html'
    context_object_name = 'new'
    permission_required = 'news.view_post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['com_post'] = Comment.objects.filter(commentPost=self.kwargs['pk']).values("commentText")
        context['pc_post'] = PostCategory.objects.filter(pcPost=self.kwargs['pk'])
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cate'] = Category.objects.all()
        return context

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


class SubsConfirm(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Category
    template_name = 'category/subs_confirm.html'
    permission_required = 'news.view_category'
    context_object_name = 'categores'


class SubsUnConfirm(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Category
    template_name = 'category/subs_unconfirm.html'
    permission_required = 'news.view_category'
    context_object_name = 'categores'


class CatigoriesView(ListView):
    template_name = 'category/categories.html'
    context_object_name = 'categories'
    queryset = Category.objects.all()


class CategoryFilterView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    permission_required = ('news.view_post', 'news.view_category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cate'] = Category.objects.all()
        return context

    def get_queryset(self):
        return Post.objects.filter(category_id=self.kwargs['pk'], public=True).order_by('-data')


@login_required
def subscribe(request, **kwargs):
    pk = kwargs.get('pk')
    category = Category.objects.get(id=pk)
    category_sub = Category.objects.filter(subscribers=request.user)
    if not category in category_sub:
        category.subscribers.add(request.user)
    return redirect('/news/categories/')


@login_required
def unsubscribe(request, **kwargs):
    pk = kwargs.get('pk')
    category = Category.objects.get(pk=pk)
    category.subscribers.remove(request.user)
    print('unsubscribe')
    return redirect('/news/categories/')
