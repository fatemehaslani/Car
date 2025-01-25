from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
   # username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))

    password1 = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}