"""
URL configuration for HiveProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls.conf import include
from django.conf import settings  
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Mainapp.urls')),
    path('accounts/', include('Accounts.urls', namespace='accounts')),
    path('dashboard/', include('DashboardPages.urls')),
    path('Teamworkspace/', include('Teamworkspace.urls')),
    path('TeamworkspaceChat/',include('TeamworkspaceChat.urls')), 
    path('matching/', include('TalentMatching.urls')),
    path('EmployersDashboard/', include('EmployersDashboard.urls')),
    path('UserProfile/', include('UserProfile.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)