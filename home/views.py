from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .forms import RegistrationForm, ContactForm
from .models import Team, Pricing
from user.models import Doctor


def home(request):
    teams = Team.objects.all()
    pricing = Pricing.objects.all()
    return render(request, 'home.html', {"header": True, "footer": True, "teams": teams, "pricing": pricing})

@method_decorator(csrf_exempt, name='dispatch')
class SignupView(View):
    form_class = RegistrationForm
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request, 'You have already registered!!', 'warning')
            return redirect('home:home')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['password1'] != cd['password2']:
                messages.error(request, 'Password and confirm password do not match!', extra_tags="danger")
                return redirect('home:login')

            # Create the user
            user = Doctor.objects.create_user(
                username=cd['username'],
                email=cd['email'],
                password=cd['password1']
            )
            messages.success(request, 'Account created successfully!', 'success')
            return redirect('home:home')

        return render(request, self.template_name, {'form': form})




@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request, 'You have already logged in', 'warning')
            return redirect('home:home')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!", 'success')
                return redirect('home:home')
            else:
                messages.error(request, "Invalid username or password.")
                redirect('login')
        return render(request, self.template_name, {'form': form})

class LogoutView(View):

    def get(self, request):
        logout(request)
        messages.success(request, 'You have been logged out successfully!', 'success')
        return redirect(reverse_lazy('home:login'))


@method_decorator(csrf_exempt, name='dispatch')
class ContactUsView(View):
    form_class = ContactForm
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            response_data = {'status': 'success', 'message': 'Your message has been sent.'}
            return JsonResponse(response_data)
        else:
            response_data = {'status': 'error', 'message': form.errors}
            return JsonResponse(response_data)

        response_data = {'status': 'error', 'message': 'Invalid request method.'}
        return JsonResponse(response_data)


