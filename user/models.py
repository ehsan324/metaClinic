# models.py
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class DoctorManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Ensure required fields for superuser creation are set
        extra_fields.setdefault('first_name', 'Admin')
        extra_fields.setdefault('last_name', 'Admin')
        extra_fields.setdefault('speciality', 'General')  # Example default

        return self.create_user(username, email, password, **extra_fields)


class Doctor(AbstractUser):
    ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    speciality = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=100)

    objects = DoctorManager()

    def __str__(self):
        return f'{self.last_name} - {self.speciality}'
class Patient(models.Model):
    ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='patients')
    gender = models.CharField(max_length=5, default='male')
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=5)



    def __str__(self):
        return f"{self.first_name} {self.last_name}"



