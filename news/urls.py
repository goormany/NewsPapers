from django.urls import path
from .views import *

urlpatterns = [
    path('', news.as_view()),
    path('<int:pk>', new.as_view(), name='news_detail'),
    path('search/', newSearch.as_view(), name='news_search'),
    path('add/', newsCreate.as_view(), name='news_add'),
    path('<int:pk>/delete/', newsDelete.as_view(), name='news_delete'),
    path('<int:pk>/edit/', newsUpdate.as_view(), name='news_update'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
]