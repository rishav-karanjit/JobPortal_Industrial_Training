from django.db import models
from django.contrib.auth.models import AbstractUser 
from datetime import  datetime,timedelta
from ckeditor.fields import RichTextField
from .choices import *
from bootstrap_datepicker_plus import DatePickerInput
# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    role=models.IntegerField(choices=(
        (1,'Employer'),
        (2,'Jobseeker'),
    ))
    avatar=models.ImageField(upload_to='images/',blank = False)
    def __str__(self):
        return(self.email)

    @property
    def is_jobseeker(self):
        return self.role==2

class JobSeekerProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    dob=models.DateField()
    gender=models.IntegerField(choices=Gender_choices,default=1)
    resume = models.FileField(upload_to="File/")
    interested_category=models.IntegerField(choices=category_choices,null=True)
    def __str__(self):
        return(self.user)

class MasterEducationLevel(models.Model):
    education=models.IntegerField(choices=Education_choices)

    def __str__(self):
        return(self.education)
    
class JobSeekerEducation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    level=models.IntegerField(choices=Education_choices)
    organization=models.CharField(max_length=80,null=True)
    nameofcourse=models.CharField(max_length=50,null=True)
    datefrom=models.DateField()
    dateto=models.DateField(blank=True,null=True)
    
class Vacancy(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    company=models.CharField(default=" ",max_length=100)
    jobcategory=models.IntegerField(choices=category_choices)
    title=models.CharField(max_length=50)
    date_added=models.DateField(auto_now_add=True)
    updated_on=models.DateField(auto_now=True)
    deadline=models.DateField(default=datetime.now() + timedelta(days=15))
    description=RichTextField()

    def __str__(self):
        return(self.title)

class Skill(models.Model):
    users=models.ForeignKey(User,on_delete=models.CASCADE)
    skills=models.CharField(max_length=50)

class TrainingInfo(models.Model):
    users=models.ForeignKey(User,on_delete=models.CASCADE)
    institute=models.CharField(max_length=100)
    course=models.CharField(max_length=60)
    
class VacancyApply(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    vacancy=models.ForeignKey(Vacancy,on_delete=models.CASCADE)
    jseeker=models.ForeignKey(JobSeekerProfile,on_delete=models.CASCADE)
    applieddate=models.DateField(auto_now=True)
    status=models.IntegerField(choices=status_choices,default=1)