# users/urls.py
from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView,index,subscribe_newsletter

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('', index, name='index'),
    path('subscribe/', subscribe_newsletter, name='subscribe_newsletter'),

]
