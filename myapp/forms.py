from django import forms
from .models import Task
from django.contrib.auth.models import User

class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'username']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name']

class RmTaskForm(forms.Form):
    def __init__(self, user):
        tasks_to_remove = forms.MultipleChoiceField(
            required=False,
            widget=forms.CheckboxSelectMultiple,
            choices=user.task_set.all(),
        )
