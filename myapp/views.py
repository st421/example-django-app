from django.shortcuts import render
from .models import User
from .forms import UserForm

def user_list(request):
    users = User.objects.all()
    form = UserForm()
    return render(request, 'user_list.html', {'users':users, 'form':form})

def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        form.save()
    users = User.objects.all()
    form = UserForm()
    return render(request, 'user_list.html', {'users':users, 'form':form})
