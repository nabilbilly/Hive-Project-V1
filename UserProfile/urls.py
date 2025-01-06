from django.urls import path
from . import views

urlpatterns = [
    # path('profile/', views.profile, name='profile'),
    path('Explore/', views.Explore, name='Explore-Interest'),
    path('ExpertedEarn/', views.ExpertedEarns, name='Experted-Earn'),
    path('YearsOfExperience/', views.YearsOfExperiences, name='Years-Of-Experience'),
    path('JobExperience/', views.JobExperiences, name='Job-Experience'),
    path('LevelOfEducation/', views.LevelOfEducations, name='Level-Of-Education'),
    path('EnglishLevel/', views.EnglishLevels, name='English-Level'),
    path('LocationOfWork/', views.LocationOfWorks, name='Location-Of-Work'),
    path('EmploymentOption/', views.EmploymentOptions, name='Employment-Option'),
    path('JobListType/', views.JobListTypes, name='Job-List-Type'),
    path('WorkSchedule/', views.WorkSchedules, name='Work-Schedule'),
    path('TeamSetup/', views.TeamSetups, name='Team-Setup'),
    path('JoinCommunity/', views.JoinCommunitys, name='Join-Community'),
    path('EmailNotification/', views.EmailNotifications, name='Email-Notification'),
    path('UpdateEnglish/', views.updateEnglish, name='UpdateEnglish'),
    path('UpdateExperted/', views.updateExperted, name='Update_Experted'),
    path('UpdateExplore/', views.updateExplore, name='Update_Explore'),
    path('UpdateExperience/', views.updateExperience, name='Update_Experience'),
    path('UpdateEducation/', views.updateEducation, name='Update_Education'),
    path('UpdateSchedule/', views.updateSchedule, name='Update_Schedule'),
    path('UpdateStatus/', views.updateWorkStatus, name='Update_WorkStatus'),
    path('UpdateTeam/', views.updateTeam, name='Update_Team'),
    
    
]