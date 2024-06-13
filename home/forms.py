from django import forms
from django.core.validators import RegexValidator, MaxLengthValidator, MinLengthValidator
from .models import ContactUsMessage
from django.db import models

password_validator = RegexValidator(
    regex=r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$",
    message='Minimum eight characters, at least one letter, one number and one special character:',
    code='invalid_password'
)


class RegistrationForm(forms.Form):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}),
    )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
    )
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        validators=[password_validator, MinLengthValidator(8), MaxLengthValidator(30)]
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}),
    )


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUsMessage
        fields = ['name', 'email', 'phone', 'message']
