from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
            if user is not None:
                if user.is_active: 
                    login(request, user)
                    return redirect('account')
            else:
                return forms.ValidationError('Invalid login', code='invalid_login')
    else:
        form = UserCreationForm()
    return render(request, 'index.html', {'form':form, 'login_form': login_form})

def account(request):
    return render(request, 'account.html')
