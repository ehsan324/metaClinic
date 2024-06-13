from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('<int:doctor_id>/', views.ProfileView.as_view(), name='profile'),
    path('patientlist/<int:doctor_id>/', views.PatientListView.as_view(), name='patientlist'),
    path('appointmentlist/<int:doctor_id>/', views.AppointmentListView.as_view(), name='appointmentlist'),
]
