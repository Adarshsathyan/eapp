from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Contact


class CustomReg(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2','email','first_name','last_name')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'