from django.db import models
from PIL import Image
from user.models import Patient, Doctor


class AboutUs(models.Model):
    email = models.EmailField()
    bio = models.TextField()
    phone = models.CharField(max_length=15, null=False, blank=False, unique=True)
    address = models.TextField(null=False)
    github = models.URLField(null=False, blank=False)
    linkedin = models.URLField(null=True, blank=False)
    instagram = models.URLField(null=True, blank=False)
    telegram = models.URLField(null=True, blank=False)

    def __str__(self):
        return self.bio


class Team(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15, unique=True)
    nick_name = models.CharField(max_length=50, unique=True)
    position = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    instagram = models.URLField(null=True, blank=True)
    telegram = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    site = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Team, self).save(*args, **kwargs)

        if self.image:
            with Image.open(self.image.path) as img:
                image = img.resize((350, 350))
                image.save(self.image.path)

    def __str__(self):
        return self.full_name


class Pricing(models.Model):
    title = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    price = models.IntegerField()
    count = models.IntegerField()
    active_email = models.IntegerField()
    module = models.IntegerField()
    automatic_scan = models.IntegerField()
    parallel_scan = models.IntegerField()

    def __str__(self):
        return self.title


class ContactUsMessage(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"from: {self.name}-{self.email}\nsubject: {self.message[:10]}"


class MedicalHistory(models.Model):
    ID = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medicalhistories')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='medicalhistories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField()
    files = models.FileField(upload_to=f'documents/{patient}-{doctor}')

    def __str__(self):
        return f'{self.patient} - {self.doctor}'

class Appointment(models.Model):
    ID = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    medicalhistory = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE, related_name='appointments', null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    notes = models.TextField()

    def __str__(self):
        return f'{self.patient} - {self.date} - {self.time}'

class Prescription(models.Model):
    ID = models.AutoField(primary_key=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='prescriptions')
    drugs = models.TextField()
    recipe = models.TextField()

    def __str__(self):
        return f'{self.drugs}'

class Bill(models.Model):
    ID = models.AutoField(primary_key=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='bills')
    price = models.DecimalField(max_digits=10, decimal_places=0)
    date = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.appointment} - {self.price} - {self.status}'
