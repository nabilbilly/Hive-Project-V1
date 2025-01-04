from django.urls import path
from . import views

urlpatterns = [
    path('employerAuth/', views.EmployerAuth, name='employer_Auth'),
    path('employersignup/', views.EmployerSignup, name='employer_signup'),
]
