from django.urls import path
from .views import news, new, newSearch, newsCreate, newsDelete, newsUpdate

urlpatterns = [
    path('', news.as_view()),
    path('<int:pk>', new.as_view(), name='news_detail'),
    path('search', newSearch.as_view(), name='news_search'),
    path('add/', newsCreate.as_view(), name='news_add'),
    path('del/<int:pk>', newsDelete.as_view(), name='news_del'),
    path('add/<int:pk>', newsUpdate.as_view(), name='news_edit'),
]