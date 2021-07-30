# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         db_table = 'django_session'


class Achievements(models.Model):
    achievementid = models.IntegerField(db_column='AchievementID', primary_key=True)  # Field name made lowercase.
    achievement = models.CharField(db_column='Achievement', max_length=75)  # Field name made lowercase.
    achievementdescription = models.TextField(db_column='AchievementDescription')  # Field name made lowercase.
    achivementdate = models.CharField(db_column='AchivementDate', max_length=100)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'tAchievements'


class Education(models.Model):
    educationid = models.IntegerField(db_column='EducationID', primary_key=True)  # Field name made lowercase.
    university = models.CharField(db_column='University', max_length=100)  # Field name made lowercase.
    startmonth = models.CharField(db_column='StartMonth', max_length=15, blank=True, null=True)  # Field name made lowercase.
    endmonth = models.CharField(db_column='EndMonth', max_length=15, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=50)  # Field name made lowercase.
    gpa = models.FloatField(db_column='GPA', blank=True, null=True)  # Field name made lowercase.
    honors = models.CharField(db_column='Honors', max_length=50, blank=True, null=True)  # Field name made lowercase.
    degreename = models.CharField(db_column='DegreeName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    endyear = models.CharField(db_column='EndYear', max_length=4)  # Field name made lowercase.
    startyear = models.CharField(db_column='StartYear', max_length=4)  # Field name made lowercase.

    class Meta:
        db_table = 'tEducation'


class Employment(models.Model):
    employmentid = models.IntegerField(db_column='EmploymentID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=50)  # Field name made lowercase.
    employer = models.CharField(db_column='Employer', max_length=100)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=75)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50)  # Field name made lowercase.
    startmonth = models.CharField(db_column='StartMonth', max_length=15, blank=True, null=True)  # Field name made lowercase.
    startyear = models.CharField(db_column='StartYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
    endmonth = models.CharField(db_column='EndMonth', max_length=15, blank=True, null=True)  # Field name made lowercase.
    endyear = models.CharField(db_column='EndYear', max_length=4, blank=True, null=True)  # Field name made lowercase.
    iscurrent = models.TextField(db_column='IsCurrent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = 'tEmployment'


class JobDescriptions(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    employmentid = models.IntegerField(db_column='EmploymentID')  # Field name made lowercase.
    jobdescription = models.TextField(db_column='JobDescription')  # Field name made lowercase.

    class Meta:
        db_table = 'tJobDescriptions'


class Projects(models.Model):
    projectid = models.IntegerField(db_column='ProjectID', primary_key=True)  # Field name made lowercase.
    projectname = models.CharField(db_column='ProjectName', max_length=100)  # Field name made lowercase.
    projectdescription = models.TextField(db_column='ProjectDescription')  # Field name made lowercase.
    startmonth = models.CharField(db_column='StartMonth', max_length=15)  # Field name made lowercase.
    endmonth = models.CharField(db_column='EndMonth', max_length=15, blank=True, null=True)  # Field name made lowercase.
    completed = models.TextField(db_column='Completed')  # Field name made lowercase. This field type is a guess.
    username = models.CharField(db_column='Username', max_length=50)  # Field name made lowercase.
    startyear = models.CharField(db_column='StartYear', max_length=4)  # Field name made lowercase.
    endyear = models.CharField(db_column='EndYear', max_length=4)  # Field name made lowercase.

    class Meta:
        db_table = 'tProjects'


class Resume(models.Model):
    version = models.IntegerField(db_column='Version')  # Field name made lowercase.
    resumename = models.CharField(db_column='ResumeName', max_length=50)  # Field name made lowercase.
    resumeid = models.IntegerField(db_column='ResumeID', primary_key=True)  # Field name made lowercase.
    resumedescription = models.TextField(db_column='ResumeDescription', blank=True, null=True)  # Field name made lowercase.
    objective = models.TextField(db_column='Objective', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tResume'


class ResumeAchievements(models.Model):
    resumeid = models.OneToOneField(Resume, models.DO_NOTHING, db_column='ResumeID', primary_key=True)  # Field name made lowercase.
    achievementid = models.IntegerField(db_column='AchievementID')  # Field name made lowercase.

    class Meta:
        db_table = 'tResumeAchievements'
        unique_together = (('resumeid', 'achievementid'),)


class ResumeEducation(models.Model):
    resumeid = models.OneToOneField(Resume, models.DO_NOTHING, db_column='ResumeID', primary_key=True)  # Field name made lowercase.
    educationid = models.IntegerField(db_column='EducationID')  # Field name made lowercase.

    class Meta:
        db_table = 'tResumeEducation'
        unique_together = (('resumeid', 'educationid'),)


class ResumeEmployment(models.Model):
    resumeid = models.OneToOneField(Resume, models.DO_NOTHING, db_column='ResumeID', primary_key=True)  # Field name made lowercase.
    employmentid = models.ForeignKey(Employment, models.DO_NOTHING, db_column='EmploymentID')  # Field name made lowercase.

    class Meta:
        db_table = 'tResumeEmployment'
        unique_together = (('resumeid', 'employmentid'),)


class ResumeProjects(models.Model):
    resumeid = models.OneToOneField(Resume, models.DO_NOTHING, db_column='ResumeID', primary_key=True)  # Field name made lowercase.
    projectid = models.ForeignKey(Projects, models.DO_NOTHING, db_column='ProjectID')  # Field name made lowercase.

    class Meta:
        db_table = 'tResumeProjects'
        unique_together = (('resumeid', 'projectid'),)


class ResumeSkills(models.Model):
    resumeid = models.OneToOneField(Resume, models.DO_NOTHING, db_column='ResumeID', primary_key=True)  # Field name made lowercase.
    skillid = models.ForeignKey('Skills', models.DO_NOTHING, db_column='SkillID')  # Field name made lowercase.

    class Meta:
        db_table = 'tResumeSkills'
        unique_together = (('resumeid', 'skillid'),)


class ResumeSocialLinks(models.Model):
    resumeid = models.OneToOneField(Resume, models.DO_NOTHING, db_column='ResumeID', primary_key=True)  # Field name made lowercase.
    linkid = models.ForeignKey('SocialLinks', models.DO_NOTHING, db_column='LinkID')  # Field name made lowercase.

    class Meta:
        db_table = 'tResumeSocialLinks'
        unique_together = (('resumeid', 'linkid'),)


class ResumeVolunteer(models.Model):
    resumeid = models.ForeignKey(Resume, models.DO_NOTHING, db_column='ResumeID')  # Field name made lowercase.
    volunteerid = models.ForeignKey('Volunteer', models.DO_NOTHING, db_column='VolunteerID')  # Field name made lowercase.

    class Meta:
        db_table = 'tResumeVolunteer'


class Skills(models.Model):
    skillid = models.BigIntegerField(db_column='SkillID', primary_key=True)  # Field name made lowercase.
    skillname = models.CharField(db_column='SkillName', max_length=75)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=15, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=20)  # Field name made lowercase.

    class Meta:
        db_table = 'tSkills'


class SocialLinks(models.Model):
    linkid = models.IntegerField(db_column='LinkID', primary_key=True)  # Field name made lowercase.
    linkurl = models.TextField(db_column='LinkURL')  # Field name made lowercase.
    linktype = models.CharField(db_column='LinkType', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tSocialLinks'


class Users(models.Model):
    username = models.CharField(db_column='Username', primary_key=True, max_length=20)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    password = models.TextField(db_column='Password', blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=13, blank=True, null=True)  # Field name made lowercase.
    mobilephone = models.CharField(db_column='MobilePhone', max_length=13, blank=True, null=True)  # Field name made lowercase.
    streetaddress1 = models.CharField(db_column='StreetAddress1', max_length=250, blank=True, null=True)  # Field name made lowercase.
    streetaddress2 = models.CharField(db_column='StreetAddress2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=5, blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'tUsers'


class Volunteer(models.Model):
    volunteerid = models.IntegerField(db_column='VolunteerID', primary_key=True)  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=75)  # Field name made lowercase.
    volunteerdescription = models.CharField(db_column='VolunteerDescription', max_length=1500)  # Field name made lowercase.
    company = models.CharField(db_column='Company', max_length=100)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50)  # Field name made lowercase.
    startmonth = models.CharField(db_column='StartMonth', max_length=15, blank=True, null=True)  # Field name made lowercase.
    endmonth = models.CharField(db_column='EndMonth', max_length=15, blank=True, null=True)  # Field name made lowercase.
    current = models.TextField(db_column='Current', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    username = models.CharField(db_column='Username', max_length=20)  # Field name made lowercase.
    startyear = models.CharField(db_column='StartYear', max_length=4)  # Field name made lowercase.
    endyear = models.CharField(db_column='EndYear', max_length=4)  # Field name made lowercase.

    class Meta:
        db_table = 'tVolunteer'
