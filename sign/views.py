from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import RegisterForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = '/news/'

@login_required
def author_me(request):
    user = request.user
    author_group = Group.objects.get(name='author')
    if not request.user.groups.filter(name='author').exists():
        author_group.user_set.add(user)
        return redirect('/')

