from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from .filters import newsFilter
from .forms import NewsForm

class news(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = '-data'
    paginate_by = 5


class new(DetailView):
    model = Post
    template_name = 'new_home.html'
    context_object_name = 'new'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['com_post'] = Comment.objects.filter(commentPost=self.kwargs['pk']).values("commentText")
        return context

class newSearch(ListView):
    model = Post
    template_name = 'new_search.html'
    context_object_name = 'newsearch'
    ordering = '-data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = newsFilter(self.request.GET, queryset=self.get_queryset())
        return context

class newsCreate(CreateView):
    template_name = 'news/news_add.html'
    form_class = NewsForm

class newsDelete(DeleteView):
    template_name = 'news/news_delete.html'
    queryset = Post.objects.all()
    context_object_name = 'newd'
    success_url = '/news/'

class newsUpdate(UpdateView):
    template_name = 'news/news_update.html'
    form_class = NewsForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)