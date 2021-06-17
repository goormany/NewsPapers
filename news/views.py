from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
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


class news(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    # paginate_by = 6

    ordering = '-data'

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

    # def form_valid(self, form):
    #     news_day_limit = 3
    #     author = Author.objects.get(author=self.request.user)
    #     if len(Post.objects.filter(author=author, post_time__date=datetime.today())) >= news_day_limit:
    #         return redirect('/news/day_limit')
    #     else:
    #         article = form.save()
    #         mail_new_post.delay(article.pk)
    #         return super().form_valid(form)


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



class CategoryFilterView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = ("news.view_category", 'news.view_post')
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorys'] = Post.objects.filter()
        return context


@login_required
def subscribe(request, **kwargs):
    pk = kwargs.get('pk')
    category = Category.objects.get(id = pk)
    category_sub = Category.objects.filter(subscribers = request.user )
    if not category in category_sub:
        category.subscribers.add(request.user )
    return redirect('/news/category/sub/confirm/')

@login_required
def unsubscribe(request, **kwargs):
    pk = kwargs.get('pk')
    category = Category.objects.get(pk = pk)
    category.subscribers.remove(request.user)
    print('unsubscribe')
    return redirect('/news/category/sub/unconfirm/')


# def mail_new_post(pid):
#     post = Post.objects.get(pk=pid)
#     subscribers = list(post.category.subscribers.all().values_list('id', flat=True))
#     subject = f'Новая статья/новость в категории {post.category}'
#     for user_id in subscribers:
#         user = User.objects.get(id=user_id)
#         email = user.email
#         html_content = render_to_string(
#             'message_for_subscribers.html',
#             {
#                 'text': post.text,
#                 'title': post.title,
#                 'category': post.category,
#                 'username': user.username,
#                 'link': f'http://127.0.0.1:8000/news/{post.id}',
#             })
#         msg = EmailMultiAlternatives(
#             subject=subject,
#             from_email='testemops@yandex.ru',
#             to=[email],
#         )
#         msg.attach_alternative(html_content, "category/category_email_push.html")  # добавляем html
#         msg.send()




