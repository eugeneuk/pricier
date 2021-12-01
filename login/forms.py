from django import forms
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(min_length=2, label="Login", widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Login'}))
    password = forms.CharField(widget=forms.PasswordInput( attrs={'class': 'form-control' , 'placeholder': 'password'} ))