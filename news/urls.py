from django.urls import path
from .views import news, new, newSearch

urlpatterns = [
    path('', news.as_view()),
    path('<int:pk>', new.as_view()),
    path('search', newSearch.as_view())
]