from django.urls import path
from .views import news

urlpatterns = [
    path('', news.as_view())
]