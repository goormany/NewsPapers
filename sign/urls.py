from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
  #  path('login/', LoginView.as_view(template_name='sign/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
   # path('signup/', RegisterView.as_view(template_name='sign/signup.html'), name='signup'),
    path('upgrade/', author_me, name='upgrade'),
]