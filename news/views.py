from .models import *
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .filters import newsFilter

class news(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = '-data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = newsFilter(self.request.GET, queryset=self.get_queryset())
        return context



class new(DetailView):
    model = Post
    template_name = 'new_home.html'
    context_object_name = 'new'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['com_post'] = Comment.objects.filter(commentPost=self.kwargs['pk']).values("commentText")
        return context
