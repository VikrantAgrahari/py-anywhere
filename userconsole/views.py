from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout , update_session_auth_hash
from .forms import LoginForm, Registeration_Form, Edit_Profile_Form
from django.contrib.auth.models import User
# Create your views here.

def login_page(request):
    form = LoginForm()
    template_name='userconsole/login.html'
    context={'form':form}
    return render(request, template_name, context)


def login_user(request):
    form= LoginForm(request.POST or None)
    template_name='userconsole/login.html'
    context={}
    if request.method=="POST":
        if form.is_valid():
            user= form.data['username']
            password= form.data['password']
            auth= authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                #messages.success(request, 'Login Successful')
                return redirect('/')
        else:
            print(form.errors)
    context={'form':form, 'form_errors':form.errors}
    return render(request,template_name,context)

        
@login_required
def logout_user(request):
    logout(request)
    #messages.success(request, ('You have logged Out Successfully!'))
    return redirect('genius:home')


def Usercreation(request):
    form = Registeration_Form(request.POST or None)
    if request.method=="POST":
        print(form)
        if form.is_valid():
            user= form.save(commit=False)
            user.save()
            print('User creation successful')
            messages.success(request,'User account regisetered successfully!')
            return redirect('user:login_page')
        else:
            print(form.errors)
    template_name='userconsole/user_create.html'
    context={'form':form,'form_errors': form.errors}
    return render(request, template_name, context)

        
def UserProfile(request):
    obj= User.objects.filter(username=request.user)
    user_data=[]
    for l in obj:
        user_data.append({
            'username':l.username,
            'email':l.email,
        })
    print(user_data)
    template_name='userconsole/userprofile.html'
    context={'data':user_data}
    return render(request,template_name,context)


def EditProfile(request):
    form= Edit_Profile_Form(request.POST or None)
    if request.method=="POST":
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Information Updated Successfully')
            return redirect('user:profile')
        else:
            print(form.errors)
    template_name='userconsole/edit_profile.html'
    context={'form':form, 'form_errors':form.errors}
    return render(request, template_name, context)
