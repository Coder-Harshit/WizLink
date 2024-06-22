#accounts/urls.py
from django.urls import path
from .views import loginPage,registrationPage
urlpatterns = [
    path('login/', loginPage, name='login'),
    path('register/', registrationPage, name='register'),
]