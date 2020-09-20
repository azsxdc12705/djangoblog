from django import forms
from django.contrib.auth.models import User
from django.db.models import fields

class SigninForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class SignupForm(forms.ModelForm):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label = 'password_confirm')

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirm')
