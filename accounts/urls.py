# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import loginPage, registrationPage, logoutPage

urlpatterns = [
    path('login/', loginPage, name='login'),
    path('register/', registrationPage, name='register'),
    path('logout/', logoutPage, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]