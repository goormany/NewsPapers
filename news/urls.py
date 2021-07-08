from django.urls import path
from .views import *

from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(news.as_view()), name='start_news'),
    path('<int:pk>', new.as_view(), name='news_detail'),
    path('search/', newSearch.as_view(), name='news_search'),
    path('add/', newsCreate.as_view(), name='news_add'),
    path('<int:pk>/delete/', newsDelete.as_view(), name='news_delete'),
    path('<int:pk>/edit/', newsUpdate.as_view(), name='news_update'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/<int:pk>/subscribe/', subscribe, name='subscribe'),
    path('category/<int:pk>/unsubscribe/', unsubscribe, name='unsubscribe'),
    path('category/sub/confirm/', SubsConfirm.as_view(), name='sub_confirm'),
    path('category/sub/unconfirm/', SubsUnConfirm.as_view(), name='sub_unconfirm'),
    path('categories/', CatigoriesView.as_view(), name = 'categories_list'),
    path('post/category/<int:pk>', cache_page(300)(CategoryFilterView.as_view()), name='cate_filter'),
]
