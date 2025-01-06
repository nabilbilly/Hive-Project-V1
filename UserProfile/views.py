from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import (
    ExploreInterest, ExpertedEarn, YearsOfExperience, JobExperience,
    LevelOfEducation, EnglishLevel, LocationOfWork, EmploymentOption,
    JobListType, WorkSchedule, TeamSetup, JoinCommunity, EmailNotification,
    UserPreference
)
from cities_light.models import Country

# Helper function to handle both GET and POST requests
@login_required
def render_with_context(request, model, template_name, context_key, preference_field, next_ui_url):
    data = model.objects.all()
    user = request.user  # Get the current authenticated user
    
    if request.method == 'POST':
        selected_option = request.POST.get(preference_field)  # Get selected option from POST data
        
        if not selected_option:
            messages.error(request, "Please select an option.")
            return render(request, template_name, {context_key: data})
        
        # Check if the user already has a preference for this field
        user_preference, created = UserPreference.objects.get_or_create(user=user)
        setattr(user_preference, preference_field, selected_option)  # Dynamically set the field
        user_preference.save()
        
        if created:
            messages.success(request, "Your preference has been saved.")
        else:
            messages.success(request, "Your preference has been updated.")
        
        return redirect(next_ui_url)  # Redirect to the next UI
    
    # For GET request, render the template with context
    context = {context_key: data}
    return render(request, template_name, context)


@login_required
def Explore(request):
    if request.method == 'POST':
        selected_interest_ids = request.POST.get('explore_interest', '')  # Get the selected options as a string
        selected_interest_ids = selected_interest_ids.split(',')  # Split the string into a list

        if not selected_interest_ids or selected_interest_ids == ['']:
            messages.error(request, "Please select your interest.")
            return render(request, 'Introduction/Exploreinterest.html', {'interest_options': ExploreInterest.objects.all()})

        if len(selected_interest_ids) > 5:  # Updated limit to 5
            messages.error(request, "You can select up to 5 interests only.")
            return render(request, 'Introduction/Exploreinterest.html', {'interest_options': ExploreInterest.objects.all()})

        # Validate input to ensure IDs are numeric
        if not all(i.isdigit() for i in selected_interest_ids):
            messages.error(request, "Invalid selection. Please try again.")
            return render(request, 'Introduction/Exploreinterest.html', {'interest_options': ExploreInterest.objects.all()})

        user = request.user  # Get the current authenticated user
        user_preference, created = UserPreference.objects.get_or_create(user=user)

        # Fetch the ExploreInterest instances
        explore_interest = ExploreInterest.objects.filter(id__in=selected_interest_ids)

        # Update the user's interests
        user_preference.explore_interests.set(explore_interest)  # Use set() to update many-to-many
        user_preference.save()

        if created:
            messages.success(request, "Your interest preferences have been saved.")
        else:
            messages.success(request, "Your interest preferences have been updated.")

        return redirect('Experted-Earn')  # Redirect to the next step

    # Render the template for a GET request
    context = {'interest_options': ExploreInterest.objects.all()}
    return render(request, 'Introduction/Exploreinterest.html', context)


@login_required
def ExpertedEarns(request):
    if request.method == 'POST':
        selected_max_salary = request.POST.get('max_salary')
        selected_min_salary = request.POST.get('min_salary')

        # Validate max_salary and min_salary
        if not selected_max_salary:
            messages.error(request, "Please select maximum salary.")
            return render(request, 'Introduction/ExpertedEarn.html')
        
        if not selected_min_salary:
            messages.error(request, "Please select minimum salary.")
            return render(request, 'Introduction/ExpertedEarn.html')
        
        if not selected_max_salary.isdigit():
            messages.error(request, "Invalid maximum salary selection.")
            return render(request, 'Introduction/ExpertedEarn.html')
        
        if not selected_min_salary.isdigit():
            messages.error(request, "Invalid minimum salary selection.")
            return render(request, 'Introduction/ExpertedEarn.html')

        # Update user preference
        user = request.user  # Get the current authenticated user
        user_preference, created = UserPreference.objects.get_or_create(user=user)

        user_preference.max_salary = int(selected_max_salary)
        user_preference.min_salary = int(selected_min_salary)
        user_preference.save()

        messages.success(request, "Your salary preferences have been set.")
        return redirect('Years-Of-Experience')  # Redirect to the next step

    return render(request, 'Introduction/ExpertedEarn.html')

@login_required
def YearsOfExperiences(request):
    if request.method == 'POST':
        selected_years_of_experience_options = request.POST.get('YearsOfExperience')  # Get the selected option from POST data
        if not selected_years_of_experience_options:
            messages.error(request, "Please select your Years Of Experience_options.")
            return render(request, 'Introduction/YearsOfExperience.html', {'YearsOfExperience_options': YearsOfExperience.objects.all()})

        user = request.user  # Get the current authenticated user
        # Check if the user already has a preference for English level
        user_preference, created = UserPreference.objects.get_or_create(user=user)

        # Fetch the JobListType instance
        try:
            years_of_experience_options = YearsOfExperience.objects.get(name=selected_years_of_experience_options)
        except YearsOfExperience.DoesNotExist:
            messages.error(request, "The selected Years Of Experience_options does not exist.")
            return render(request, 'Introduction/YearsOfExperience.html', {'YearsOfExperience_options': YearsOfExperience.objects.all()})

        # Update the user's English levels
        user_preference.years_experience.set([years_of_experience_options])  # Use set() to update many-to-many
        user_preference.save()

        if created:
            messages.success(request, "Your Years Of Experience_options preference has been saved.")
        else:
            messages.success(request, "Your Years Of Experience_options preference has been updated.")

        return redirect('Job-Experience')  # Redirect to the next step

    # Render the template for a GET request
    context = {'YearsOfExperience_options': YearsOfExperience.objects.all()}
    return render(request, 'Introduction/YearsOfExperience.html', context)
  
@login_required
def JobExperiences(request):
    
    context = {'JobExperience_options': JobExperience.objects.all()}
    
    if request.method == 'POST':
        selected_job_experience = request.POST.get('job_experience')  # Get the selected option from POST data
        if not selected_job_experience:
            messages.error(request, "Please select your job experience.")
            return render(request, 'Introduction/JobExperience.html', context)

        user = request.user  # Get the current authenticated user
        # Check if the user already has a preference for English level
        user_preference, created = UserPreference.objects.get_or_create(user=user)

        # Fetch the JobExperience instance
        try:
            job_experiences = JobExperience.objects.get(name=selected_job_experience)
        except JobExperience.DoesNotExist:
            messages.error(request, "The selected job experience does not exist.")
            return render(request, 'Introduction/JobExperience.html', context)

        # Update the user's job experience
        user_preference.experiences.set([job_experiences])  # Use set() to update many-to-many
        user_preference.save()

        if created:
            messages.success(request, "Your job experience preference has been saved.")
        else:
            messages.success(request, "Your job experience preference has been updated.")

        return redirect('Level-Of-Education')  # Redirect to the next step

    # Render the template for a GET request
    
    return render(request, 'Introduction/JobExperience.html', context)

@login_required
def LevelOfEducations(request):
    if request.method == 'POST':
        selected_level_of_education = request.POST.get('level_education')  # Get the selected option from POST data
        if not selected_level_of_education:
            messages.error(request, "Please select your level of education option.")
            return render(request, 'Introduction/LevelOfEducation.html', {'LevelOfEducation_options': LevelOfEducation.objects.all()})

        user = request.user  # Get the current authenticated user
        # Check if the user already has a preference for English level
        user_preference, created = UserPreference.objects.get_or_create(user=user)

        # Fetch the EmploymentOption instance
        try:
            level_of_education = LevelOfEducation.objects.get(name=selected_level_of_education)
        except LevelOfEducation.DoesNotExist:
            messages.error(request, "The selected level of education does not exist.")
            return render(request, 'Introduction/LevelOfEducation.html', {'LevelOfEducation_options': LevelOfEducation.objects.all()})

        # Update the user's English levels
        user_preference.languages.set([level_of_education])  # Use set() to update many-to-many
        user_preference.save()

        if created:
            messages.success(request, "Your level of education preference has been saved.")
        else:
            messages.success(request, "Your level of education preference has been updated.")

        return redirect('English-Level')  # Redirect to the next step

    # Render the template for a GET request
    context = {'LevelOfEducation_options': LevelOfEducation.objects.all()}
    return render(request, 'Introduction/LevelOfEducation.html', context)


@login_required
def EnglishLevels(request):
    if request.method == 'POST':
        selected_english_level = request.POST.get('english_level')  # Get the selected option from POST data
        if not selected_english_level:
            messages.error(request, "Please select your English level.")
            return render(request, 'Introduction/EnglishLevel.html', {'EnglishLevel_options': EnglishLevel.objects.all()})

        user = request.user  # Get the current authenticated user
        # Check if the user already has a preference for English level
        user_preference, created = UserPreference.objects.get_or_create(user=user)

        # Fetch the EnglishLevel instance
        try:
            selected_level = EnglishLevel.objects.get(name=selected_english_level)
        except EnglishLevel.DoesNotExist:
            messages.error(request, "The selected English level does not exist.")
            return render(request, 'Introduction/EnglishLevel.html', {'EnglishLevel_options': EnglishLevel.objects.all()})

        # Update the user's English levels
        user_preference.english_levels.set([selected_level])  # Use set() to update many-to-many
        user_preference.save()

        if created:
            messages.success(request, "Your English level preference has been saved.")
        else:
            messages.success(request, "Your English level preference has been updated.")

        return redirect('Location-Of-Work')  # Redirect to the next step

    # Render the template for a GET request
    context = {'EnglishLevel_options': EnglishLevel.objects.all()}
    return render(request, 'Introduction/EnglishLevel.html', context)

@login_required
def LocationOfWorks(request):
    if request.method == 'POST':
        selected_location_ids = request.POST.get('location_work', '')  # Get the selected options as a string
        selected_location_ids = selected_location_ids.split(',')
        
        selected_country_ids = request.POST.get('countries', '')  # Get the selected options as a string
        selected_country_ids = selected_country_ids.split(',') 

        if not selected_location_ids or selected_location_ids == ['']:
            messages.error(request, "Please select your location.")
            return render(request, 'Introduction/LocationOfWork.html', {'interest_options': LocationOfWork.objects.all(),
                                                                        'Country': Country.objects.all()
                                                                        })
        if not selected_country_ids or selected_country_ids == ['']:
            messages.error(request, "Please select your continent.")
            return render(request, 'Introduction/LocationOfWork.html', {'interest_options': LocationOfWork.objects.all(),
                                                                        'Country': Country.objects.all()
                                                                        })

        if len(selected_location_ids) > 5:  # Updated limit to 5
            messages.error(request, "You can select up to 5 interests only.")
            return render(request, 'Introduction/LocationOfWork.html', {'interest_options': LocationOfWork.objects.all(),
                                                                        'Country': Country.objects.all()
                                                                        })
        
        if len(selected_country_ids) > 5:  # Updated limit to 5
            messages.error(request, "You can select up to 5 interests only.")
            return render(request, 'Introduction/LocationOfWork.html', {'interest_options': LocationOfWork.objects.all(),
                                                                        'Country': Country.objects.all()
                                                                        })
                                                               

        # Validate input to ensure IDs are numeric
        if not all(i.isdigit() for i in selected_location_ids):
            messages.error(request, "Invalid selection with location. Please try again.")
            return render(request, 'Introduction/LocationOfWork.html', {'interest_options': LocationOfWork.objects.all(),
                                                                        'Country': Country.objects.all()
                                                                        })
        
        # Validate input to ensure IDs are numeric
        if not all(i.isdigit() for i in selected_country_ids):
            messages.error(request, "Invalid selection with continent. Please try again.")
            return render(request, 'Introduction/LocationOfWork.html', {'interest_options': LocationOfWork.objects.all(),
                                                                        'Country': Country.objects.all()
                                                                        })

        user = request.user  # Get the current authenticated user
        user_preference, created = UserPreference.objects.get_or_create(user=user)

        # Fetch the ExploreInterest instances
        work_location = LocationOfWork.objects.filter(id__in=selected_location_ids)
        work_country = Country.objects.filter(id__in=selected_country_ids)

        # Update the user's interests
        user_preference.work_locations.set(work_location)
        
        user_preference.country_location.set(work_country)
        
        user_preference.save()

        if created:
            messages.success(request, "Your interest preferences have been saved.")
        else:
            messages.success(request, "Your interest preferences have been updated.")

        return redirect('Employment-Option')  # Redirect to the next step

    # Render the template for a GET request
    context = {'interest_options': LocationOfWork.objects.all(),
               'Country': Country.objects.all()
               }
    return render(request, 'Introduction/LocationOfWork.html', context)
@login_required
def EmploymentOptions(request):
    if request.method == 'POST':
        selected_employment_option = request.POST.get('employment_option')  # Get the selected option from POST data
        if not selected_employment_option:
            messages.error(request, "Please select your employment option.")
            return render(request, 'Introduction/EmploymentOption.html', {'employment_options': EmploymentOption.objects.all()})

        user = request.user  # Get the current authenticated user
        # Check if the user already has a preference for English level
        user_preference, created = UserPreference.objects.get_or_create(user=user)

        # Fetch the EmploymentOption instance
        try:
            employment_option = EmploymentOption.objects.get(name=selected_employment_option)
        except EmploymentOption.DoesNotExist:
            messages.error(request, "The selected employment option does not exist.")
            return render(request, 'Introduction/EmploymentOption.html', {'employment_options': EmploymentOption.objects.all()})

        # Update the user's English levels
        user_preference.employment_options.set([employment_option])  # Use set() to update many-to-many
        user_preference.save()

        if created:
            messages.success(request, "Your employment option preference has been saved.")
        else:
            messages.success(request, "Your employment option preference has been updated.")

        return redirect('Job-List-Type')  # Redirect to the next step

    # Render the template for a GET request
    context = {'employment_options': EmploymentOption.objects.all()}
    return render(request, 'Introduction/EmploymentOption.html', context)

@login_required
def JobListTypes(request):
    if request.method == 'POST':
        selected_JobListType_options = request.POST.get('JobListType_options')  # Get the selected option from POST data
        if not selected_JobListType_options:
            messages.error(request, "Please select your job preference.")
            return render(request, 'Introduction/JobListType.html', {'JobListType_options': JobListType.objects.all()})

        user = request.user  # Get the current authenticated user
        # Check if the user already has a preference for English level
        user_preference, created = UserPreference.objects.get_or_create(user=user)

        # Fetch the JobListType instance
        try:
            JobListType_options = JobListType.objects.get(name=selected_JobListType_options)
        except JobListType.DoesNotExist:
            messages.error(request, "The selected job type list does not exist.")
            return render(request, 'Introduction/JobListType.html', {'JobListType_options': JobListType.objects.all()})

        # Update the user's English levels
        user_preference.job_types.set([JobListType_options])  # Use set() to update many-to-many
        user_preference.save()

        if created:
            messages.success(request, "Your job type list preference has been saved.")
        else:
            messages.success(request, "Your job type list preference has been updated.")

        return redirect('Work-Schedule')  # Redirect to the next step

    # Render the template for a GET request
    context = {'JobListType_options': JobListType.objects.all()}
    return render(request, 'Introduction/JobListType.html', context)
    
@login_required
def WorkSchedules(request):
    if request.method == 'POST':
        # Get the selected work schedule option from POST data
        selected_work_schedule_option = request.POST.get('work_schedule_option')  
        if not selected_work_schedule_option:
            messages.error(request, "Please select your work schedule.")
            return render(request, 'Introduction/WorkSchedule.html', {'work_schedule_options': WorkSchedule.objects.all()})

        user = request.user  # Get the current authenticated user

        # Check if the user already has a preference for work schedule
        user_preference, created = UserPreference.objects.get_or_create(user=user)

        # Fetch the work schedule instance
        try:
            work_schedule_option = WorkSchedule.objects.get(name=selected_work_schedule_option)
        except WorkSchedule.DoesNotExist:
            messages.error(request, "The selected work schedule does not exist.")
            return render(request, 'Introduction/WorkSchedule.html', {'work_schedule_options': WorkSchedule.objects.all()})

        # Update the user's work schedule preferences
        user_preference.work_schedules.set([work_schedule_option])  # Use set() to update many-to-many
        user_preference.save()

        if created:
            messages.success(request, "Your work schedule preference has been saved.")
        else:
            messages.success(request, "Your work schedule preference has been updated.")

        return redirect('Team-Setup')  # Redirect to the next step

    # Render the template for a GET request
    context = {'work_schedule_options': WorkSchedule.objects.all()}
    return render(request, 'Introduction/WorkSchedule.html', context)
    

@login_required
def TeamSetups(request):
    if request.method == 'POST':
        selected_TeamSetup = request.POST.get('team_setup')  # Get the selected option from POST data
        if not selected_TeamSetup:
            messages.error(request, "Please select your team_setups.")
            return render(request, 'Introduction/TeamSetup.html', {'TeamSetup_options': TeamSetup.objects.all()})

        user = request.user  # Get the current authenticated user
        # Check if the user already has a preference for team_setups
        user_preference, created = UserPreference.objects.get_or_create(user=user)

        # Fetch the TeamSetup instance
        try:
            team_setup = TeamSetup.objects.get(name=selected_TeamSetup)
        except TeamSetup.DoesNotExist:
            messages.error(request, "The selected TeamSetup does not exist.")
            return render(request, 'Introduction/TeamSetup.html', {'TeamSetup_options': TeamSetup.objects.all()})

        # Update the user's TeamSetup
        user_preference.team_setups.set([team_setup])  # Use set() to update many-to-many
        user_preference.save()

        if created:
            messages.success(request, "Your TeamSetup preference has been saved.")
        else:
            messages.success(request, "Your TeamSetup preference has been updated.")

        return redirect('Join-Community')  # Redirect to the next step

    # Render the template for a GET request
    context = {'TeamSetup_options': TeamSetup.objects.all()}
    return render(request, 'Introduction/TeamSetup.html', context)
   
   
@login_required
def JoinCommunitys(request):
    return render_with_context(request, JoinCommunity, 'Introduction/JoinCommunity.html', 'JoinCommunity_options', 'join_community', '/email-notifications')

@login_required
def EmailNotifications(request):
    if request.method == 'POST':
        selected_email_notification = request.POST.get('email')  # Get the selected option from POST data
        if not selected_email_notification:
            messages.error(request, "please select to receive a new email notification.")
            return render(request, 'Introduction/EmailNotification.html')

        user = request.user  # Get the current authenticated user
        # Check if the user already has a preference for English level
        user_preference, created = UserPreference.objects.get_or_create(user=user)

        # Fetch the EmploymentOption instance
        try:
            email_notification = EmailNotification.objects.get(name=selected_email_notification)
        except EmailNotification.DoesNotExist:
            messages.error(request, "please select to receive a new email notification")
            return render(request, 'Introduction/EmailNotification.html')

        # Update the user's English levels
        user_preference.email_notifications.set([email_notification])  # Use set() to update many-to-many
        user_preference.save()

        if created:
            messages.success(request, "Your have allow  has been saved.")
        else:
            messages.success(request, "Yourpreference has been updated.")

        return redirect('dashboard:job_view')  # Redirect to the next step

    # Render the template for a GET request

    return render(request, 'Introduction/EmailNotification.html')  # Replace with the final UI URL


def updateEnglish(request):
    context = {
        'active_page': 'language',
        'EnglishLevel_options': EnglishLevel.objects.all()
    }
    return render(request, 'portfolioProfileRecentActivity/EnglishLevel.html',context)

def updateExperted(request):
    context = {
        'active_page': 'earning',  # Set this dynamically based on the current page
    }
    return render(request, 'portfolioProfileRecentActivity/ExpertedEarn.html',context)
@login_required
def updateExplore(request):
    # Fetch the user's stored preference
    user_preference = UserPreference.objects.filter(user=request.user).first()
    stored_preference_ids = user_preference.explore_interests.values_list('id', flat=True) if user_preference else []

    context = {
        'active_page': 'category',
        'interest_options': ExploreInterest.objects.all(),
        'stored_preference_ids': stored_preference_ids  
    }
    return render(request, 'portfolioProfileRecentActivity/Exploreinterest.html', context)

def updateExperience(request):
    context = {
        'active_page': 'experience',
        'YearsOfExperience_options': YearsOfExperience.objects.all(),
        'JobExperience_options': JobExperience.objects.all()
        
    }
    return render(request, 'portfolioProfileRecentActivity/JobExperience.html',context)

def updateEducation(request):
    context = {
        'active_page': 'education',
        'LevelOfEducation_options': LevelOfEducation.objects.all()
    }
    return render(request, 'portfolioProfileRecentActivity/LevelOfEducation.html',context)

def updateTeam(request):
    context = {
        'active_page': 'team_setup', 
        'TeamSetup_options': TeamSetup.objects.all()
    }
    return render(request, 'portfolioProfileRecentActivity/TeamSetup.html',context)

def updateSchedule(request):
    context = {
        'active_page': 'work_location',
        'interest_options': LocationOfWork.objects.all(),
        'Country': Country.objects.all()# Set this dynamically based on the current page
    }
    return render(request, 'portfolioProfileRecentActivity/WorkSchedule.html',context)

def updateWorkStatus(request):
    context = {
        'active_page': 'work_status',
        'employment_options': EmploymentOption.objects.all(),
        'JobListType_options': JobListType.objects.all(),
        'work_schedule_options': WorkSchedule.objects.all()
        
    }
    return render(request, 'portfolioProfileRecentActivity/Workstatus.html',context)



