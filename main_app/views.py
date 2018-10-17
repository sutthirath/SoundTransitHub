from django.shortcuts import render, redirect
from .models import Account
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Function based views

def index(request):
    login_form = AuthenticationForm(request.POST)
    form = UserCreationForm(request.POST)
    if (request.method == 'POST'):
        # Signup form
        if request.POST.get('submit') == 'sign_up':
            form = UserCreationForm(request.POST)
            if (form.is_valid()):
                form.save()
                # Log the user in
                return redirect('account')
        # Login form
        elif request.POST.get('submit') == 'sign_in':
            if form.is_valid():
                u = form.cleaned_data['username']
                p = form.cleaned_data['password']
                user = authenticate(username = u, password = p)
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
        form = UserCreationForm()
    return render(request, 'index.html', {'form':form, 'login_form': login_form})

def account(request):
    return render(request, 'account.html')

    personal_info = {
        'first_name'
        'last_name'
        'password'
    }

    pod_info = {

    }

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