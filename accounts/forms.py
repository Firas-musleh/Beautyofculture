from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['image',  'address']


class UserCreatForm(UserCreationForm):
    username = forms.CharField(max_length=150, label='Användnamn')
    first_name = forms.CharField(max_length=150, label='förnamn')
    last_name = forms.CharField(max_length=150, label='efternamn')
    password1 = forms.CharField(max_length=150, label='Lösenord 1')
    password2 = forms.CharField(max_length=150, label='Lösenord 2')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']
        help_texts = {'username': 'hej'}
