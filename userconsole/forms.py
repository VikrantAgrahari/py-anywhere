from django import forms
from django.contrib.auth import user_logged_in

class LoginForm(forms.Form):
    username= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control'}))

    # def __init__(self, *args, **kwargs):
    #     super(LoginForm, self).__init__(*args, **kwargs)
    #     self.fields['username']=forms.CharField( label='Username', widget=forms.CharField(attrs={'class':'form-control'}))
    #     self.fields['password']=forms.CharField( label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))