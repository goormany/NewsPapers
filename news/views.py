from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from .filters import newsFilter
from .forms import NewsForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

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
    template_name = 'news/news_add.html'
    form_class = NewsForm
    permission_required = 'news.add_post'

class newsDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'news/news_delete.html'
    queryset = Post.objects.all()
    context_object_name = 'newd'
    success_url = '/news/'
    permission_required = 'news.delete_post'

class newsUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'news/news_update.html'
    form_class = NewsForm
    permission_required = 'news.change_post'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

@login_required
def subscribe(request, pk):
    category = Category.objects.get(id=request.POST.get('category_id'))

    if category.subscribers.filter(id=request.user.id).exists():
        category.subscribers.remove(request.user)

    else:
        category.subscribers.add(request.user)
    return redirect(request.META.get('HTTP_REFERER'))