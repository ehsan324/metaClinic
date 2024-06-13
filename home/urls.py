from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('contact/', views.ContactUsView.as_view(), name="contact"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
]
