from django.contrib.auth.forms import UserCreationForm # type: ignore

from django import forms # type: ignore
from django.contrib.auth.models import User # type: ignore

class UserSignupForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']