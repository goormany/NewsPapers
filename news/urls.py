from django.urls import path
from .views import news, new

urlpatterns = [
    path('', news.as_view()),
    path('<int:pk>', new.as_view()),
]