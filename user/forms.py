# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Doctor, Patient

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Doctor
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'speciality', 'phone_number', 'address']


class CreatePatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'age', 'doctor', 'gender', 'phone_number', 'address', 'blood_type']
