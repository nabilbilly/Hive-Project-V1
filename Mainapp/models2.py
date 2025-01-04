# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountsCategory(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'Accounts_category'


class AccountsCommunity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'Accounts_community'


class AccountsCountry(models.Model):
    code = models.CharField(primary_key=True, max_length=2)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Accounts_country'


class AccountsEducationlevel(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'Accounts_educationlevel'


class AccountsEmploymentoption(models.Model):
    name = models.CharField(unique=True, max_length=50)
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'Accounts_employmentoption'


class AccountsOtp(models.Model):
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField()
    is_used = models.BooleanField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Accounts_otp'


class AccountsOtpverification(models.Model):
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Accounts_otpverification'


class AccountsProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.CharField(max_length=200, blank=True, null=True)
    user_profile = models.ForeignKey('AccountsUserprofile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Accounts_project'


class AccountsSkill(models.Model):
    name = models.CharField(unique=True, max_length=100)
    user_profile = models.ForeignKey('AccountsUserprofile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Accounts_skill'


class AccountsUserprofile(models.Model):
    user = models.OneToOneField('AuthUser', models.DO_NOTHING)
    has_logged_in = models.BooleanField()
    address = models.TextField()
    bio = models.TextField()
    email = models.CharField(unique=True, max_length=254, blank=True, null=True)
    english_proficiency = models.CharField(max_length=25, blank=True, null=True)
    experience_level = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    include_work_anywhere = models.BooleanField()
    include_work_location = models.BooleanField()
    is_verified = models.BooleanField()
    last_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    max_salary = models.IntegerField()
    min_salary = models.IntegerField()
    newsletter_signup = models.BooleanField()
    phone_number = models.CharField(max_length=20)
    portfolio_url = models.CharField(max_length=200, blank=True, null=True)
    preferred_work_style = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.CharField(max_length=100, blank=True, null=True)
    salary_type = models.CharField(max_length=10)
    skills = models.CharField(max_length=255, blank=True, null=True)
    team_setup = models.CharField(max_length=20)
    verification_token = models.CharField(max_length=255, blank=True, null=True)
    years_of_experience = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Accounts_userprofile'


class AccountsUserprofileEducationLevels(models.Model):
    userprofile = models.ForeignKey(AccountsUserprofile, models.DO_NOTHING)
    educationlevel = models.ForeignKey(AccountsEducationlevel, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Accounts_userprofile_education_levels'
        unique_together = (('userprofile', 'educationlevel'),)


class AccountsUserprofileEmploymentOptions(models.Model):
    userprofile = models.ForeignKey(AccountsUserprofile, models.DO_NOTHING)
    employmentoption = models.ForeignKey(AccountsEmploymentoption, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Accounts_userprofile_employment_options'
        unique_together = (('userprofile', 'employmentoption'),)


class AccountsUserprofilePreferredCountries(models.Model):
    userprofile = models.ForeignKey(AccountsUserprofile, models.DO_NOTHING)
    country = models.ForeignKey(AccountsCountry, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Accounts_userprofile_preferred_countries'
        unique_together = (('userprofile', 'country'),)


class AccountsUserprofileSelectedCategories(models.Model):
    userprofile = models.ForeignKey(AccountsUserprofile, models.DO_NOTHING)
    category = models.ForeignKey(AccountsCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Accounts_userprofile_selected_categories'
        unique_together = (('userprofile', 'category'),)


class AccountsUserprofileskill(models.Model):
    skill = models.ForeignKey(AccountsSkill, models.DO_NOTHING)
    user_profile = models.ForeignKey(AccountsUserprofile, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Accounts_userprofileskill'
        unique_together = (('user_profile', 'skill'),)


class AccountsUserprogress(models.Model):
    step1_completed = models.BooleanField()
    step2_completed = models.BooleanField()
    step3_completed = models.BooleanField()
    user = models.OneToOneField('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Accounts_userprogress'


class AccountsWorkschedulepreferences(models.Model):
    flexible_hours = models.BooleanField()
    nine_to_five = models.BooleanField()
    user = models.OneToOneField('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Accounts_workschedulepreferences'


class DashboardpagesCompany(models.Model):
    company_name = models.CharField(max_length=255)
    logo = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=200)
    description = models.TextField()
    user = models.OneToOneField('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DashboardPages_company'


class DashboardpagesFile(models.Model):
    file = models.CharField(max_length=100)
    filename = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField()
    filetype = models.CharField(max_length=50)
    uploaded_by = models.ForeignKey('AuthUser', models.DO_NOTHING)
    workspace = models.ForeignKey('DashboardpagesWorkspace', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DashboardPages_file'


class DashboardpagesInterestcategory(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'DashboardPages_interestcategory'


class DashboardpagesJob(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salary_min = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    salary_max = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    is_remote = models.BooleanField()
    min_salary = models.IntegerField(blank=True, null=True)
    max_salary = models.IntegerField(blank=True, null=True)
    job_type = models.CharField(max_length=50)
    posted_date = models.DateTimeField()
    application_deadline = models.DateTimeField(blank=True, null=True)
    posted_by = models.ForeignKey('AuthUser', models.DO_NOTHING)
    workspace = models.ForeignKey('DashboardpagesWorkspace', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DashboardPages_job'


class DashboardpagesJobSkills(models.Model):
    job = models.ForeignKey(DashboardpagesJob, models.DO_NOTHING)
    skill = models.ForeignKey(AccountsSkill, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DashboardPages_job_skills'
        unique_together = (('job', 'skill'),)


class DashboardpagesJobapplication(models.Model):
    applied_at = models.DateTimeField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    job = models.ForeignKey('DashboardpagesJoblisting', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DashboardPages_jobapplication'
        unique_together = (('user', 'job'),)


class DashboardpagesJoblisting(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=50)
    experience_level = models.CharField(max_length=100)
    salary_min = models.FloatField()
    salary_max = models.FloatField()
    description = models.TextField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'DashboardPages_joblisting'


class DashboardpagesJobreport(models.Model):
    reason = models.CharField(max_length=255)
    additional_info = models.TextField()
    reported_at = models.DateTimeField()
    job = models.ForeignKey(DashboardpagesJoblisting, models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DashboardPages_jobreport'


class DashboardpagesJobsearchpreferences(models.Model):
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    user = models.OneToOneField('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DashboardPages_jobsearchpreferences'


class DashboardpagesJobskill(models.Model):
    job = models.ForeignKey(DashboardpagesJob, models.DO_NOTHING)
    skill = models.ForeignKey(AccountsSkill, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DashboardPages_jobskill'
        unique_together = (('job', 'skill'),)


class DashboardpagesLocation(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DashboardPages_location'


class DashboardpagesMessage(models.Model):
    timestamp = models.DateTimeField()
    message = models.TextField()
    sender = models.ForeignKey('AuthUser', models.DO_NOTHING)
    workspace = models.ForeignKey('DashboardpagesWorkspace', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DashboardPages_message'


class DashboardpagesUserintroduction(models.Model):
    interests = models.JSONField()
    expected_salary = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    salary_type = models.CharField(max_length=10)
    years_experience = models.IntegerField(blank=True, null=True)
    education_level = models.CharField(max_length=50, blank=True, null=True)
    english_level = models.CharField(max_length=20, blank=True, null=True)
    preferred_location = models.CharField(max_length=50, blank=True, null=True)
    employment_type = models.CharField(max_length=50, blank=True, null=True)
    work_schedule = models.CharField(max_length=50, blank=True, null=True)
    team_setup = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.OneToOneField('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DashboardPages_userintroduction'


class DashboardpagesUserjobprofile(models.Model):
    employment_type = models.CharField(max_length=50)
    english_level = models.CharField(max_length=50)
    expected_salary = models.IntegerField(blank=True, null=True)
    interests = models.TextField()
    years_of_experience = models.IntegerField()
    education_level = models.CharField(max_length=100)
    preferred_location = models.CharField(max_length=255)
    work_schedule = models.CharField(max_length=50)
    email_notifications = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.OneToOneField('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DashboardPages_userjobprofile'


class DashboardpagesUserjobprofileSkills(models.Model):
    userjobprofile = models.ForeignKey(DashboardpagesUserjobprofile, models.DO_NOTHING)
    skill = models.ForeignKey(AccountsSkill, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DashboardPages_userjobprofile_skills'
        unique_together = (('userjobprofile', 'skill'),)


class DashboardpagesWorkspace(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_active = models.BooleanField()
    owner = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DashboardPages_workspace'


class DashboardpagesWorkspaceimage(models.Model):
    image = models.CharField(max_length=100)
    workspace = models.ForeignKey(DashboardpagesWorkspace, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DashboardPages_workspaceimage'


class DashboardpagesWorkspacemember(models.Model):
    role = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    role_description = models.TextField()
    joined_at = models.DateTimeField()
    is_active = models.BooleanField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    workspace = models.ForeignKey(DashboardpagesWorkspace, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'DashboardPages_workspacemember'
        unique_together = (('workspace', 'user'),)


class MainappEmailnotification(models.Model):
    emailsend = models.BooleanField(db_column='emailSend')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mainapp_emailnotification'


class MainappEmploymentoption(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Mainapp_employmentoption'


class MainappEnglishlevel(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Mainapp_englishlevel'


class MainappExpertedearn(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Mainapp_expertedearn'


class MainappExploreinterest(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Mainapp_exploreinterest'


class MainappJobexperience(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Mainapp_jobexperience'


class MainappJoblisttype(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Mainapp_joblisttype'


class MainappJoincommunity(models.Model):

    class Meta:
        managed = False
        db_table = 'Mainapp_joincommunity'


class MainappJoincommunityTeam(models.Model):
    joincommunity = models.ForeignKey(MainappJoincommunity, models.DO_NOTHING)
    team = models.ForeignKey('TeamworkspaceTeam', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Mainapp_joincommunity_team'
        unique_together = (('joincommunity', 'team'),)


class MainappLevelofeducation(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Mainapp_levelofeducation'


class MainappLocationofwork(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Mainapp_locationofwork'


class MainappTeamsetup(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Mainapp_teamsetup'


class MainappUserpreference(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.OneToOneField('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Mainapp_userpreference'


class MainappUserpreferenceCountryLocation(models.Model):
    userpreference = models.ForeignKey(MainappUserpreference, models.DO_NOTHING)
    country = models.ForeignKey('CitiesLightCountry', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Mainapp_userpreference_country_location'
        unique_together = (('userpreference', 'country'),)


class MainappUserpreferenceEmailNotifications(models.Model):
    userpreference = models.ForeignKey(MainappUserpreference, models.DO_NOTHING)
    emailnotification = models.ForeignKey(MainappEmailnotification, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Mainapp_userpreference_email_notifications'
        unique_together = (('userpreference', 'emailnotification'),)


class MainappUserpreferenceEmploymentOptions(models.Model):
    userpreference = models.ForeignKey(MainappUserpreference, models.DO_NOTHING)
    employmentoption = models.ForeignKey(MainappEmploymentoption, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Mainapp_userpreference_employment_options'
        unique_together = (('userpreference', 'employmentoption'),)


class MainappUserpreferenceEnglishLevels(models.Model):
    userpreference = models.ForeignKey(MainappUserpreference, models.DO_NOTHING)
    englishlevel = models.ForeignKey(MainappEnglishlevel, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Mainapp_userpreference_english_levels'
        unique_together = (('userpreference', 'englishlevel'),)


class MainappUserpreferenceExpectedEarnings(models.Model):
    userpreference = models.ForeignKey(MainappUserpreference, models.DO_NOTHING)
    expertedearn = models.ForeignKey(MainappExpertedearn, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Mainapp_userpreference_expected_earnings'
        unique_together = (('userpreference', 'expertedearn'),)


class MainappUserpreferenceExperiences(models.Model):
    userpreference = models.ForeignKey(MainappUserpreference, models.DO_NOTHING)
    jobexperience = models.ForeignKey(MainappJobexperience, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Mainapp_userpreference_experiences'
        unique_together = (('userpreference', 'jobexperience'),)


class MainappUserpreferenceExploreInterests(models.Model):
    userpreference = models.ForeignKey(MainappUserpreference, models.DO_NOTHING)
    exploreinterest = models.ForeignKey(MainappExploreinterest, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Mainapp_userpreference_explore_interests'
        unique_together = (('userpreference', 'exploreinterest'),)


class MainappUserpreferenceJobTypes(models.Model):
    userpreference = models.ForeignKey(MainappUserpreference, models.DO_NOTHING)
    joblisttype = models.ForeignKey(MainappJoblisttype, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Mainapp_userpreference_job_types'
        unique_together = (('userpreference', 'joblisttype'),)


class MainappUserpreferenceLanguages(models.Model):
    userpreference = models.ForeignKey(MainappUserpreference, models.DO_NOTHING)
    levelofeducation = models.ForeignKey(MainappLevelofeducation, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Mainapp_userpreference_languages'
        unique_together = (('userpreference', 'levelofeducation'),)


class MainappUserpreferenceTeamSetups(models.Model):
    userpreference = models.ForeignKey(MainappUserpreference, models.DO_NOTHING)
    teamsetup = models.ForeignKey(MainappTeamsetup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Mainapp_userpreference_team_setups'
        unique_together = (('userpreference', 'teamsetup'),)


class MainappUserpreferenceTeams(models.Model):
    userpreference = models.ForeignKey(MainappUserpreference, models.DO_NOTHING)
    team = models.ForeignKey('TeamworkspaceTeam', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Mainapp_userpreference_teams'
        unique_together = (('userpreference', 'team'),)


class MainappUserpreferenceWorkSchedules(models.Model):
    userpreference = models.ForeignKey(MainappUserpreference, models.DO_NOTHING)
    workschedule = models.ForeignKey('MainappWorkschedule', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Mainapp_userpreference_work_schedules'
        unique_together = (('userpreference', 'workschedule'),)


class MainappUserpreferenceYearsExperience(models.Model):
    userpreference = models.ForeignKey(MainappUserpreference, models.DO_NOTHING)
    yearsofexperience = models.ForeignKey('MainappYearsofexperience', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Mainapp_userpreference_years_experience'
        unique_together = (('userpreference', 'yearsofexperience'),)


class MainappWorkschedule(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Mainapp_workschedule'


class MainappYearsofexperience(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Mainapp_yearsofexperience'


class TalentmatchingCandidatevector(models.Model):
    skill_vector = models.JSONField()
    experience_vector = models.JSONField()
    updated_at = models.DateTimeField()
    user = models.OneToOneField('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TalentMatching_candidatevector'


class TalentmatchingJobvector(models.Model):
    skill_vector = models.JSONField()
    experience_vector = models.JSONField()
    updated_at = models.DateTimeField()
    job = models.OneToOneField(DashboardpagesJoblisting, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TalentMatching_jobvector'


class TalentmatchingMatchpreference(models.Model):
    min_salary = models.IntegerField(blank=True, null=True)
    max_salary = models.IntegerField(blank=True, null=True)
    preferred_locations = models.JSONField()
    remote_only = models.BooleanField()
    job_types = models.JSONField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.OneToOneField('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TalentMatching_matchpreference'


class TalentmatchingMatchscore(models.Model):
    score = models.FloatField()
    skill_match_score = models.FloatField()
    experience_match_score = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    candidate = models.ForeignKey('AuthUser', models.DO_NOTHING)
    job = models.ForeignKey(DashboardpagesJoblisting, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TalentMatching_matchscore'
        unique_together = (('candidate', 'job'),)


class TalentmatchingSkillvector(models.Model):
    vector = models.JSONField()
    updated_at = models.DateTimeField()
    skill = models.ForeignKey(AccountsSkill, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TalentMatching_skillvector'


class TeamworkspacechatMessage(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField()
    team = models.ForeignKey('TeamworkspaceTeam', models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TeamworkspaceChat_message'


class TeamworkspaceTeam(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField()
    slug = models.CharField(unique=True, max_length=100)
    unique_id = models.CharField(unique=True, max_length=32)
    created_at = models.DateTimeField()
    created_by = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Teamworkspace_team'


class TeamworkspaceTeammembership(models.Model):
    description = models.TextField()
    specifyrole = models.CharField(db_column='SpecifyRole', max_length=100)  # Field name made lowercase.
    joined_at = models.DateTimeField()
    role = models.CharField(max_length=20)
    team = models.ForeignKey(TeamworkspaceTeam, models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Teamworkspace_teammembership'
        unique_together = (('team', 'user'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_login = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CitiesLightCity(models.Model):
    name_ascii = models.CharField(max_length=200)
    slug = models.CharField(max_length=50)
    geoname_id = models.IntegerField(unique=True, blank=True, null=True)
    alternate_names = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    longitude = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    region = models.ForeignKey('CitiesLightRegion', models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey('CitiesLightCountry', models.DO_NOTHING)
    population = models.BigIntegerField(blank=True, null=True)
    feature_code = models.CharField(max_length=10, blank=True, null=True)
    search_names = models.TextField()
    timezone = models.CharField(max_length=40, blank=True, null=True)
    subregion = models.ForeignKey('CitiesLightSubregion', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities_light_city'
        unique_together = (('region', 'subregion', 'name'), ('region', 'subregion', 'slug'),)


class CitiesLightCountry(models.Model):
    name_ascii = models.CharField(max_length=200)
    slug = models.CharField(max_length=50)
    geoname_id = models.IntegerField(unique=True, blank=True, null=True)
    alternate_names = models.TextField(blank=True, null=True)
    code2 = models.CharField(unique=True, max_length=2, blank=True, null=True)
    code3 = models.CharField(unique=True, max_length=3, blank=True, null=True)
    continent = models.CharField(max_length=2)
    tld = models.CharField(max_length=5)
    phone = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'cities_light_country'


class CitiesLightRegion(models.Model):
    name_ascii = models.CharField(max_length=200)
    geoname_id = models.IntegerField(unique=True, blank=True, null=True)
    alternate_names = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    geoname_code = models.CharField(max_length=50, blank=True, null=True)
    country = models.ForeignKey(CitiesLightCountry, models.DO_NOTHING)
    slug = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cities_light_region'
        unique_together = (('country', 'name'), ('country', 'slug'),)


class CitiesLightSubregion(models.Model):
    name = models.CharField(max_length=200)
    name_ascii = models.CharField(max_length=200)
    slug = models.CharField(max_length=50)
    geoname_id = models.IntegerField(unique=True, blank=True, null=True)
    alternate_names = models.TextField(blank=True, null=True)
    display_name = models.CharField(max_length=200)
    geoname_code = models.CharField(max_length=50, blank=True, null=True)
    country = models.ForeignKey(CitiesLightCountry, models.DO_NOTHING)
    region = models.ForeignKey(CitiesLightRegion, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities_light_subregion'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
