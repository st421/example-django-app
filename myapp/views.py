from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import UserProfile
from .forms import UserSignupForm, UserLoginForm, AddTaskForm, RmTaskForm

def home(request):
    return render(request, 'home.html', {})

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return profile(request)
            else:
                #add invalid password message
                return new_login(request, UserLoginForm())
        else:
            return new_login(request, UserLoginForm())
    else:
        return new_login(request, UserLoginForm())

def new_login(request, form):
    return render(request, 'login.html', {'form':form})

@login_required(login_url='login.html')
def profile(request):
    add_form = AddTaskForm()
    user = request.user
    points = user.userprofile.points
    #rm_form = RmTaskForm(user)
    return render(request, 'profile.html', {'user':user, 'add_form':add_form, 'tasks':user.task_set.all(), 'points':points})

def signup(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return profile(request)
        else:
            return render(request, 'signup.html', {'form':form})
    else:
        form = UserSignupForm()
        return render(request, 'signup.html', {'form':form})

def new_task(request):
    form = AddTaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        return profile(request)
    else:
        return render(request, '404.html', {})

def rm_task(request):
    form = RmTaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        return profile(request)
    else:
        return render(request, '404.html', {})
