from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from .filters import newsFilter
from .forms import NewsForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
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

#class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
 #   model = Category
  #  template_name = 'category/subscribe.html'
   # context_object_name = 'categories'
    #permission_required = 'news.view_category'
#
 #   def get(self, request, *args, **kwargs):
  #      return render(request, 'category/subscribe.html')
#
 #   def post(self, request, *args, **kwargs):
  #      subscribe = Category.objects.get(name=request.POST['category'])
   #     subscriber = self.request.user
    #    subscribe.subscribers.add(subscriber)
     #   subscribe.save()
#
 #       send_mail(
  #          subject=subscribe.name,
   #         message=f'hello {subscribe.name}',
    #        from_email='testemops@yandex.ru',
     #       recipient_list=[subscribe.email],
      #  )
       # return redirect('/news/')

@login_required
def subscribe_view(request):
    category = get_object_or_404(Category, id=request.POST.get('category_id'))
    if category.category_subscriber.filter(id=request.user.id).exists():
        category.category_subscriber.remove(request.user)
        sub_trigger = False
    else:
        category.category_subscriber.add(request.user)
        sub_trigger = True
    html_context_category = {'sub_category_name': category, 'sub_category_user': request.user}
    if sub_trigger:
        html_content = render_to_string('category/subs_confirm.html', html_context_category)
        msg = EmailMultiAlternatives(
            subject=f'Подписка на категорию {html_context_category["sub_category_name"]}',
            from_email='testemops@yandex.ru',
            to=['vigertop@yandex.ru']
        )
        msg.attach_alternative(html_content, 'test/html')

        msg.send()
    else:
        html_content = render_to_string('category/subs_unconfirm.html', html_context_category)
        msg = EmailMultiAlternatives(
            subject=f'Подписка на категорию {html_context_category["sub_category_name"]}',
            from_email='testemops@yandex.ru',
            to=['vigertop@yandex.ru']
        )
        msg.attach_alternative(html_content, 'test/html')

        msg.send()
    return redirect('news')