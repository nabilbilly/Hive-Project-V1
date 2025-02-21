from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUp, name='SignUp'),
    path('login/', views.Login, name='Login'),
    path('introduction/', views.Introduction, name='Introduction'), 
    path('logout/', views.logout_view, name='LogoutUser'),
    path('resend-verification-mail/', views.resend_verification, name='resend_verification'),
    path('ForgotPasswordEmail/', views.ForgotPasswordEmail, name='ForgotPasswordEmail'),
    path('verify-otp/<int:user_id>/', views.VerifyOTP, name='verify-otp'),
    path('PasswordReset/<int:user_id>/', views.PasswordReset, name='PasswordReset'),
    path('reset/<uidb64>/<token>/', views.verify_email, name='verify_email'),
   
]
