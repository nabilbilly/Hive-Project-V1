from django.utils.html import format_html
from django.contrib import admin
from .models import (
    ExploreInterest,
    ExpertedEarn,
    YearsOfExperience,
    JobExperience,
    LevelOfEducation,
    EnglishLevel,
    LocationOfWork,
    EmploymentOption,
    JobListType,
    WorkSchedule,
    TeamSetup,
    JoinCommunity,

    UserPreference
)

@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'user', 
        'profile_image_preview',  # Display the image preview
        'get_experiences', 
        'get_languages',
        'get_english_levels',
        'get_work_locations',
        'get_employment_options',
        'get_job_types',
        'get_country_options',
        'get_work_schedules',
        'get_team_setups',
        'get_explore_interests',
        'get_expected_earnings',
        'get_years_experience',
        'get_teams',
        'get_bio_data',
        'get_email_notifications',
        'created_at',
        'updated_at'
    )  
    search_fields = ('user__username', 'user__email')  # Allows searching by username and email

    # Custom method to display the image
    def profile_image_preview(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.profile_image.url)
        return "No Image"
    profile_image_preview.short_description = "Profile Image"

    # Custom methods to handle ManyToMany fields
    def get_experiences(self, obj):
        return ", ".join([str(experience) for experience in obj.experiences.all()])
    get_experiences.short_description = "Experiences"

    def get_languages(self, obj):
        return ", ".join([str(language) for language in obj.languages.all()])
    get_languages.short_description = "Languages"

    def get_english_levels(self, obj):
        return ", ".join([str(level) for level in obj.english_levels.all()])
    get_english_levels.short_description = "English Levels"

    def get_work_locations(self, obj):
        return ", ".join([str(location) for location in obj.work_locations.all()])
    get_work_locations.short_description = "Work Locations"

    def get_country_options(self, obj):
        return ", ".join([str(countries) for countries in obj.country_location.all()])
    get_country_options.short_description = "Country Options"


    def get_employment_options(self, obj):
        return ", ".join([str(employment) for employment in obj.employment_options.all()])
    get_employment_options.short_description = "Employment Options"

    def get_job_types(self, obj):
        return ", ".join([str(job_type) for job_type in obj.job_types.all()])
    get_job_types.short_description = "Job Types"

    def get_work_schedules(self, obj):
        return ", ".join([str(schedule) for schedule in obj.work_schedules.all()])
    get_work_schedules.short_description = "Work Schedules"

    def get_team_setups(self, obj):
        return ", ".join([str(setup) for setup in obj.team_setups.all()])
    get_team_setups.short_description = "Team Setups"

    def get_explore_interests(self, obj):
        return ", ".join([str(interest) for interest in obj.explore_interests.all()])
    get_explore_interests.short_description = "Explore Interests"

    def get_expected_earnings(self, obj):
        return ", ".join([str(earning) for earning in obj.expected_earnings.all()])
    get_expected_earnings.short_description = "Expected Earnings"

    def get_years_experience(self, obj):
        return ", ".join([str(year) for year in obj.years_experience.all()])
    get_years_experience.short_description = "Years of Experience"

    def get_teams(self, obj):
        return ", ".join([str(team) for team in obj.team.all()])
    get_teams.short_description = "Teams"
    
    #Nabil change This 
    # def get_bio_data(self, obj):
    #     return ", ".join([str(bio_data) for bio_data in obj.bio_data])
    # get_bio_data.short_description = "Bio Data"
    
    def get_bio_data(self, obj):
        if obj.bio_data:  # Check if bio_data is not None
            return ", ".join([str(bio_data) for bio_data in obj.bio_data])
        return "No bio data available"  # Return a default message if bio_data is None

     
    def get_min_salary(self, obj):
        return ", ".join([str(min_salary) for min_salary in obj.min_salary])
    get_min_salary.short_description = "min salary"

    def get_max_salary(self, obj):
        return ", ".join([str(max_salary) for max_salary in obj.max_salary])
    get_max_salary.short_description = "max salary"


    def get_email_notifications(self, obj):
        return "Enabled" if obj.email_notifications else "Disabled"
    get_email_notifications.short_description = "Email Notifications"

# Register the other models in the admin panel
admin.site.register(ExploreInterest)
admin.site.register(ExpertedEarn)
admin.site.register(YearsOfExperience)
admin.site.register(JobExperience)
admin.site.register(LevelOfEducation)
admin.site.register(EnglishLevel)
admin.site.register(LocationOfWork)
admin.site.register(EmploymentOption)
admin.site.register(JobListType)
admin.site.register(WorkSchedule)
admin.site.register(TeamSetup)
admin.site.register(JoinCommunity)
# admin.site.register(EmailNotification)