from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout , update_session_auth_hash
from .forms import LoginForm
# Create your views here.

def login_page(request):
    form = LoginForm()
    print('get into login page')
    template_name='userconsole/login.html'
    context={'form':form}
    return render(request, template_name, context)


def login_user(request):
    form= LoginForm(request.POST or None)
    if request.method=="POST":
        user= form.data['username']
        password= form.data['password']
        auth= authenticate(request, username=user, password=password)
        if auth is not None:
            login(request, auth)
            print('Login Successful')
            messages.success(request, 'Login Successful')
            return redirect('/')
        else:
            messages.success(request, ('Makesure your Username or Password is correct!'))
            return redirect('user:login_page')
            print('Not login')
    else:
        messages.error(request,'Request method is wrong')

        

def logout_user(request):
    logout(request)
    messages.success(request, ('You have logged Out Successfully!'))
    return redirect('genius:home')