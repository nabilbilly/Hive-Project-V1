from django.urls import path
from . import views

urlpatterns = [
    path('', views.Talentpage, name='Talent-page'),
    path('DevCommunity/', views.DevCommunityView, name='DevCommunity-page'),
    path('DonatePage/', views.DonatePage, name='Donate-Page'),
    path('AboutUs/', views.AboutUsPage, name='About_us-page'),
    path('employers/', views.Employerspage, name='Employers-Page'),
    # path('Explore/', views.Explore, name='Explore-Interest'),
    # path('ExpertedEarn/', views.ExpertedEarns, name='Experted-Earn'),
    # path('YearsOfExperience/', views.YearsOfExperiences, name='Years-Of-Experience'),
    # path('JobExperience/', views.JobExperiences, name='Job-Experience'),
    # path('LevelOfEducation/', views.LevelOfEducations, name='Level-Of-Education'),
    # path('EnglishLevel/', views.EnglishLevels, name='English-Level'),
    # path('LocationOfWork/', views.LocationOfWorks, name='Location-Of-Work'),
    # path('EmploymentOption/', views.EmploymentOptions, name='Employment-Option'),
    # path('JobListType/', views.JobListTypes, name='Job-List-Type'),
    # path('WorkSchedule/', views.WorkSchedules, name='Work-Schedule'),
    # path('TeamSetup/', views.TeamSetups, name='Team-Setup'),
    # path('JoinCommunity/', views.JoinCommunitys, name='Join-Community'),
    # path('EmailNotification/', views.EmailNotifications, name='Email-Notification'),
]
