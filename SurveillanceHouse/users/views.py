# users/views.py
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import CustomUser,NewsletterSubscriber
from .forms import YourCustomRegistrationForm,NewsletterSubscriptionForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import JsonResponse




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

def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Check if the email is already subscribed
        if NewsletterSubscriber.objects.filter(email=email).exists():
            message = 'You are already subscribed to the newsletter.'
            return JsonResponse({'message': message, 'status': 'warning'})

        subscriber = NewsletterSubscriber(email=email)
        subscriber.save()
        message = 'Subscription successful! Thank you for subscribing.'
        return JsonResponse({'message': message, 'status': 'success'})

    return JsonResponse({'message': 'Invalid request', 'status': 'error'})


