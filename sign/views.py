from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import RegisterForm

class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = '/news/'