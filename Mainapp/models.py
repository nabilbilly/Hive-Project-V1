from django.db import models
# from django.contrib.auth.models import User
# from Teamworkspace.models import Team
# from django.utils.timezone import now 
# from cities_light.models import Country



# class ExploreInterest(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class ExpertedEarn(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class YearsOfExperience(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class JobExperience(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class LevelOfEducation(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class EnglishLevel(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class LocationOfWork(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class EmploymentOption(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class JobListType(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class WorkSchedule(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class TeamSetup(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class JoinCommunity(models.Model):
#     team = models.ManyToManyField(
#         Team,
#         related_name="join_community_members"  # Unique related_name
#     )

#     def __str__(self):
#         return f"Join request for {self.team.name}"

# class EmailNotification(models.Model):
#     emailSend = models.BooleanField()

#     def __str__(self):
#         return "Enabled" if self.emailSend else "Disabled"

# class UserPreference(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="preferences")
#     experiences = models.ManyToManyField(JobExperience, related_name="users")
#     languages = models.ManyToManyField(LevelOfEducation, related_name="users")
#     english_levels = models.ManyToManyField(EnglishLevel, related_name="users")
#     country_location = models.ManyToManyField(Country, related_name="users")
#     work_locations = models.ManyToManyField(LocationOfWork, related_name="users")
#     job_types = models.ManyToManyField(JobListType, related_name="users")
#     work_schedules = models.ManyToManyField(WorkSchedule, related_name="users")
#     employment_options = models.ManyToManyField(EmploymentOption, related_name="users")
#     team_setups = models.ManyToManyField(TeamSetup, related_name="users")
#     explore_interests = models.ManyToManyField(ExploreInterest, related_name="users")
#     expected_earnings = models.ManyToManyField(ExpertedEarn, related_name="users")
#     years_experience = models.ManyToManyField(YearsOfExperience, related_name="users")
#     teams = models.ManyToManyField(Team, related_name="users")
#     email_notifications = models.BooleanField(default=True, editable=False)
#     created_at = models.DateTimeField(default=now, editable=False)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Preferences for {self.user.username}"

#     def __str__(self):
#         return "Enabled" if self.emailSend else "Disabled"
