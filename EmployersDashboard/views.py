from django.shortcuts import render

def EmployerAuth(request):
   
    return render(request, 'Employers/EmployerAuth.html')

def EmployerIntromessage(request):
    
    return render(request, 'Employers/EmployerIntromessage.html')

def EmployerSignup(request):
    
    return render(request, 'Employers/EmployersSignup.html')

def EmployerSignupSecond(request):
    
    return render(request, 'Employers/EmployersSignup2.html')
