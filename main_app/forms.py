from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class MultipleForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())

class LoginForm(MultipleForm):
    username = forms.CharField(max_length=50)
    password = forms.PasswordInput()

class SignupForm(MultipleForm):
    form = UserCreationForm