from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .filters import newsFilter
from .forms import *
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.core.cache import cache


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


class new(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Post
    template_name = 'new_home.html'
    context_object_name = 'new'
    permission_required = 'news.view_post'
    # form = CommentForm
    #
    # def post(self, request, *args, **kwargs):
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         post = self.get_object()
    #         form.instance.user = request.user
    #         form.instance.post = post
    #         form.save()
    #
    #         return redirect(reverse('news_detail', kwargs={
    #             'pk': post.pk
    #         }))
    #     else:
    #         HttpResponse('Данные не валидные')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # post_comments_count = Comment.objects.all().filter(post=self.object.id).count()
        # post_comments = Comment.objects.all().filter(post=self.object.id)
        # context['com_post'] = Comment.objects.filter(commentPost=self.kwargs['pk']).values("commentText")
        context['pc_post'] = PostCategory.objects.filter(pcPost=self.kwargs['pk'])
        # context.update({
        #     'form': self.form,
        #     'post_comments': post_comments,
        #     'post_comments_count': post_comments_count
        # })
        return context




    def get_object(self, *args, **kwargs):
        obj = cache.get(f"new-{self.kwargs['pk']}", None)

        if not obj:
            obj = super().get_object(queryset=self.get_queryset())
            cache.set(f"new-{self.kwargs['pk']}", obj)

        return obj


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
