from django.shortcuts import render, redirect
from django import forms
from .forms import Details
from .models import Account
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

# Function based views

def index(request):
    if (request.method == 'POST'):   
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            u = login_form.cleaned_data['username']
            p = login_form.cleaned_data['password']
            user = authenticate(request, username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/account')
                else:
                    print("The account has been disabled.")
                    return HttpResponseRedirect('/')
        else:
            print("The username and/or password is incorrect.")
            return HttpResponseRedirect('/')
    else:
        login_form = AuthenticationForm()
    return render(request, 'index.html', {'login_form':login_form})


def signup(request):
    if (request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if (form.is_valid()):
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/details/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def details_view(request):
    if (request.method == 'POST'):
        form = Details(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account/')
    else:
        form = Details()
    return render(request, 'details.html', {'form': form})

def account(request):
    return render(request, 'account.html')

class PodCreate(CreateView):
    model = Account
    fields = '__all__'

class PodUpdate(UpdateView):
    model = Account
    fields = '__all__'

class PodDelete(DeleteView):
    model = Account
    success_url = '/account'

def main(request):
    return render(request, 'main.html')