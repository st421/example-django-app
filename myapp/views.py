from django.shortcuts import render
from .models import User
from .forms import UserForm

def home(request):
    return render(request, 'home.html', {})

def get_user(request):
    user_name = "Susan"
    u = User.objects.get(pk=user_name)
    return render(request, 'user_thanks.html', {'user':u})

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users':users})


def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        user = form.save()
        return render(request, 'user_thanks.html', {'user':user})
    else:
        form = UserForm()
        return render(request, 'add_user.html', {'form':form})
