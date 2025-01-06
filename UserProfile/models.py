from django.db import models
from django.contrib.auth.models import User
from Teamworkspace.models import Team
from django.utils.timezone import now
from cities_light.models import Country


class ExploreInterest(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ExpertedEarn(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class YearsOfExperience(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class JobExperience(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class LevelOfEducation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class EnglishLevel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class LocationOfWork(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class EmploymentOption(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class JobListType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class WorkSchedule(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TeamSetup(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class JoinCommunity(models.Model):
    team = models.ManyToManyField(
        Team,
        related_name="join_community_members"  # Unique related_name
    )

    def __str__(self):
        return "Join request for teams"


class EmailNotification(models.Model):
    emailSend = models.BooleanField()

    def __str__(self):
        return "Enabled" if self.emailSend else "Disabled"


class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="preferences")
    profile_image = models.ImageField(upload_to='user_preferences/images/', blank=True, null=True)
    experiences = models.ManyToManyField(JobExperience, related_name="user_experiences")
    languages = models.ManyToManyField(LevelOfEducation, related_name="user_languages")
    english_levels = models.ManyToManyField(EnglishLevel, related_name="user_english_levels")
    country_location = models.ManyToManyField(Country, related_name="user_country_locations")
    work_locations = models.ManyToManyField(LocationOfWork, related_name="user_work_locations")
    job_types = models.ManyToManyField(JobListType, related_name="user_job_types")
    work_schedules = models.ManyToManyField(WorkSchedule, related_name="user_work_schedules")
    employment_options = models.ManyToManyField(EmploymentOption, related_name="user_employment_options")
    team_setups = models.ManyToManyField(TeamSetup, related_name="user_team_setups")
    explore_interests = models.ManyToManyField(ExploreInterest, related_name="user_explore_interests")
    expected_earnings = models.ManyToManyField(ExpertedEarn, related_name="user_expected_earnings")
    years_experience = models.ManyToManyField(YearsOfExperience, related_name="user_years_experience")
    min_salary = models.IntegerField(default=0)
    max_salary = models.IntegerField(default=0)
    bio_data = models.TextField( blank=True, null=True)
    team = models.ManyToManyField(Team, related_name="user_teams")
    email_notifications = models.BooleanField(default=False, editable=False)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Preferences for {self.user.username}"

    def __str__(self):
        return "Enabled" if self.emailSend else "Disabled"