from django import forms
from django.contrib.auth import user_logged_in
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm

class LoginForm(forms.Form):
    username= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control'}))

    # def __init__(self, *args, **kwargs):
    #     super(LoginForm, self).__init__(*args, **kwargs)
    #     self.fields['username']=forms.CharField( label='Username', widget=forms.CharField(attrs={'class':'form-control'}))
    #     self.fields['password']=forms.CharField( label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

class Registeration_Form(UserCreationForm):
    class Meta:
        model= User
        fields = ('username', 'first_name', 'last_name', 'email' , 'password1', 'password2',)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'username': None,
            'email': None,
            'password1': None,
            'password2': None,
        }

class Edit_Profile_Form(UserChangeForm):
    class Meta:
        model=User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
    
