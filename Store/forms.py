from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Store.models import CustomUser

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'password1', 'password2', 'address', 'nickname_tg', 'telephone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'nickname_tg': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '@nickname_telegram'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter telephone'}),
        }

class UserLoginForm(AuthenticationForm):
    #name = forms.CharField(
    #    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'})
    #)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'})
    )