from django.contrib.auth import login ,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from account.models import Account
from django import forms







class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ("email", 
                  "nick_name",
                  "password1",
                  "password2")
       
