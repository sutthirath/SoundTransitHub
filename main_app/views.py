from django.shortcuts import render, redirect
from django import forms
from .forms import LoginForm, SignupForm, MultipleForm
from .multiforms import MultiFormsView
from .models import Account
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy


# Function based views

def index(request):
    return render(request, 'index.html')

# def login_view(request):
#     login_form = AuthenticationForm(request.POST)
#     if login_form.is_valid():
#         u = login_form.cleaned_data['username']
#         p = login_form.cleaned_data['password']
#         user = authenticate(username = u, password = p)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect('/account')
#             else:
#                 print("The account has been disabled.")
#                 return HttpResponseRedirect('/')
#     else:
#         print("The username and/or password is incorrect.")
#         return HttpResponseRedirect('/')

# def signup_view(request):
#     form = UserCreationForm(request.POST)
#     if (request.method == 'POST'):
#         print('POSSTTTTTTTTT')
#         # Signup form
#         if request.POST.get('submit') == 'sign_up':
#             form = UserCreationForm(request.POST)
#             print("sign up - im right here!!!!!!!!!")
#             if (form.is_valid()):
#                 user = form.save()
#                 login(request, user)
#                 return redirect('account')
#             else:
#                 print('FAILED VALIDATIONS++++++++++++++++++++++++++=')
#     else:
#         print("ELSEEEEEEEE - im right here!!!!!!!!!")
#         return render(request, 'index.html', {'form':form})

# TEST
def form_redir(request):
    return render(request, 'index.html')

def multiple_forms(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        signup_form = SignupForm(request.POST)
        if login_form.is_valid() or signup_form.is_valid():
            # Do the needful
            return HttpResponseRedirect(reverse('form-redirect') )
    else:
        login_form = LoginForm()
        signup_form = SignupForm()
            
    return render(request, 'index.html', {
        'login_form': login_form,
        'signup_form': signup_form,
    })

class SignupLoginView(MultiFormsView):
    template_name = 'index.html'
    form_classes = {'login_view': LoginForm,
                    'signup_view': SignupForm}
    success_url = 'account/'

    def get_context_data(self, **kwargs):
        context = super(SignupLoginView, self).get_context_data(**kwargs)
        context.update({"some_context_value": 'blah blah blah',
                        "some_other_context_value": 'blah'})
        return context

    def login_form_valid(self, form):
        return form.login(self.request, redirect_url=self.get_success_url())

    def signup_form_valid(self, form):
        user = form.save(self.request)
        return form.signup(self.request, user, self.get_success_url())

# TEST




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