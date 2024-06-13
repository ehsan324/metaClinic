from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from .models import Doctor
from django.contrib import messages
from home.models import Appointment




class ProfileView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('home:login')
    def get(self, request, doctor_id):
        doctor = Doctor.objects.get(pk=doctor_id)
        lists = doctor.patients.all()
        alists = doctor.appointments.all()
        return render(request, 'profile.html', {"lists": lists, 'alists': alists})

class PatientListView(View):
    template_name = 'patient_list.html'
    def get(self, request, doctor_id):
        doctor = Doctor.objects.get(pk=doctor_id)
        lists = doctor.patients.all()
        return render(request, self.template_name, {'lists': lists})


class AppointmentListView(View):
    template_name = 'appointment_list.html'
    def get(self, request, doctor_id):
        doctor = Doctor.objects.get(pk=doctor_id)
        lists = doctor.appointments.all()
        return render(request, self.template_name, {'lists': lists})