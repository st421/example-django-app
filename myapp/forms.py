from django import forms
from .models import Task
from django.contrib.auth.models import User

class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def save(self):
        user = super(UserSignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name']
