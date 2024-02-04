# users/views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import YourCustomRegistrationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages



class UserRegistrationView(SuccessMessageMixin, CreateView):
    model = CustomUser
    template_name = 'register.html'
    form_class = YourCustomRegistrationForm
    success_url = reverse_lazy('login')
    success_message = "Registration successful. Please log in."

    def form_invalid(self, form):
        messages.error(self.request, 'Registration failed. Please check the form.')
        return super().form_invalid(form)
class UserLoginView(LoginView):
    template_name = 'login.html'

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid login credentials. Please try again.')
        return super().form_invalid(form)

class UserLogoutView(LogoutView):
    template_name = 'home/index.html'
def index(request):
    return render(request, 'home/index.html')
