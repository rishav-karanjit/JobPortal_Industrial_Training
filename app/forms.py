from django import forms
from django.contrib.auth.forms import UserCreationForm
from .choices import *
from .models import User,JobSeekerProfile

class Signupform(UserCreationForm):
    class Meta:
        model=User
        fields=('email','first_name','last_name','role','avatar')
        
class JSeekerForm(forms.Form):
    dob=forms.DateField() 
    gender = forms.ChoiceField(choices = Gender_choices)
    resume = forms.FileField()
    interested_category=forms.ChoiceField(choices=(
        (0,'-------'),
        (1,'IT/Telecomunication'),
        (2,'Construction'),
        (3,'Medical'),
        (4,'Banking/ Insurance/ Financial Services'),
        (5,'Teaching/ Education'),
        (6,'General Management/ Administration'),   
    ),initial='0')

class EducationForm(forms.Form):
    level=forms.ChoiceField(choices=Education_choices)
    organization=forms.CharField(max_length=80)
    nameofcourse=forms.CharField(max_length=50)
    datefrom=forms.DateField()
    dateto=forms.DateField()

class VacancyAppliedForm(forms.Form):
    pass

