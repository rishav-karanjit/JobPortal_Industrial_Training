from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import generic
from .models import User,Vacancy,JobSeekerProfile,JobSeekerEducation,Skill,TrainingInfo,VacancyApply
from .forms import Signupform,JSeekerForm,EducationForm,VacancyAppliedForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
class Homepage(generic.ListView):
    template_name='home.html'
    model= Vacancy
    context_object_name='vacancys'

class EmpDashboard(LoginRequiredMixin,generic.UpdateView):
    model=User
    fields=['email','avatar','first_name','last_name']
    template_name='Emp_dash.html'
    
    def form_valid(self,form):
        instance=form.save()
        return redirect('home')

class JobSeekerDashboard(LoginRequiredMixin,generic.ListView):
    model= JobSeekerProfile
    template_name='jobseeker-dashboard.html'
    context_object_name='job'
    def get_queryset(self):
        return JobSeekerProfile.objects.filter(user_id=self.request.user.id)

@login_required
def UpdateJobSeeker(request, pk):
    try:
        user = request.user
        jseeker = JobSeekerProfile.objects.get(user_id=pk)
        form = JSeekerForm(request.POST or None,request.FILES or None,initial={'dob':jseeker.dob, 'gender':jseeker.gender, 'resume':jseeker.resume, 'interested_category':jseeker.interested_category})
        if request.user == jseeker.user:
            if request.method == 'POST':
                if form.is_valid():
                    jseeker.dob = form.cleaned_data['dob']
                    jseeker.gender = form.cleaned_data['gender']
                    try:
                        jseeker.resume = request.FILES['resume']
                    except MultiValueDictKeyError:
                        pass
                    jseeker.interested_category = form.cleaned_data['interested_category']
                    jseeker.save()
                    return redirect('home')
                            
    except JobSeekerProfile.DoesNotExist:
        form = JSeekerForm(request.POST or None,request.FILES or None)
        if request.method == 'POST':
            if form.is_valid():
                user = request.user    
                dob = form.cleaned_data['dob']
                gender=form.cleaned_data['gender']
                interested_category=form.cleaned_data['interested_category']
                jseeker = JobSeekerProfile(dob=dob,gender=gender,user=user,resume=request.FILES['resume'],interested_category=interested_category)
                jseeker.save()
                return redirect('home')  
    return render(request, 'jobseeker-update.html', {'form':form})

class EduInfo(LoginRequiredMixin,generic.ListView):
    model=JobSeekerEducation
    template_name='edu-info.html'
    context_object_name='educations'
    def get_queryset(self):
        user_id = self.request.user.id
        if user_id is None:
            return []
        return JobSeekerEducation.objects.filter(user_id=self.request.user)

class Vacancy_create(LoginRequiredMixin,generic.CreateView):
    model= Vacancy
    template_name='post_vacancy.html'
    fields=['jobcategory','title','deadline','description','company']
    def form_valid(self,form):
        instance=form.save(commit=False)
        instance.user_id=self.request.user.id
        instance.save()
        return redirect('vacancy')

class My_vacancy(LoginRequiredMixin,generic.ListView):
    model= Vacancy
    template_name='my_vacancy.html'
    context_object_name='vacancys'
    def get_queryset(self):
        user_id = self.request.user.id
        if user_id is None:
            return []
        return Vacancy.objects.filter(user=self.request.user)
  

class SignUpView(generic.CreateView):
    form_class=Signupform
    template_name='registration/signup.html'
    success_url=reverse_lazy('home')

class VacancyUpdateView(LoginRequiredMixin,generic.UpdateView):
    model= Vacancy
    template_name='updatevacancy.html'
    fields=['jobcategory','title','deadline','description','company']
    
    def form_valid(self,form):
        instance=form.save()
        return redirect('my_vacancy')

class VacancyDeleteView(LoginRequiredMixin,generic.DeleteView):
    model= Vacancy
    template_name='deletevacancy.html'
    success_url='/'

class Search(generic.ListView):
    def get(self, request, *args, **kwargs):
        try:
            search_term=request.GET['search_term']
            search_result=Vacancy.objects.filter(
                Q(title__contains=search_term)|
                Q(description__contains=search_term))
            context={
                'search_term': search_term,
                'vacancys':search_result
            }
            return render(request,'search.html',context)
        except KeyError:
            return redirect('Home')

class SkillSet(LoginRequiredMixin,generic.ListView):
    model= Skill
    template_name='jseeker-skills.html'
    context_object_name='skills'
    def get_queryset(self):
        return Skill.objects.filter(users_id=self.request.user.id)

class AddSkillSet(LoginRequiredMixin,generic.CreateView):
    model=Skill
    template_name='jseeker-update-skills.html'
    fields=['skills']

    def form_valid(self,form):
        instance=form.save(commit=False)
        instance.users_id=self.request.user.id
        instance.save()
        return redirect('skillset')

class DeleteSkillSet(LoginRequiredMixin,generic.DeleteView):
    model= Skill
    template_name='delete-skills.html'
    success_url=reverse_lazy('skillset')

class AddEduInfo(LoginRequiredMixin,generic.CreateView):
    model= JobSeekerEducation
    template_name='edu-info-add.html'
    fields=['level','organization','nameofcourse','datefrom','dateto']
    def form_valid(self,form):
        instance=form.save(commit=False)
        instance.user_id=self.request.user.id
        instance.save()
        return redirect('education-info',self.request.user.id)

class UpdateEduInfo(LoginRequiredMixin,generic.UpdateView):
    model= JobSeekerEducation
    template_name='edu-info-update.html'
    fields=['level','organization','nameofcourse','datefrom','dateto']
    
    def form_valid(self,form):
        instance=form.save()
        return redirect('education-info',self.request.user.id)

class DeleteEduInfo(LoginRequiredMixin,generic.DeleteView):
    model= JobSeekerEducation
    template_name='edu-info-delete.html'
    context_object_name='edu'
    success_url=reverse_lazy('education-info')

class TrainingInfo(LoginRequiredMixin,generic.ListView):
    model= TrainingInfo
    template_name='training-info.html'
    context_object_name='trainings'
    def get_queryset(self):
        return TrainingInfo.objects.filter(users_id=request.self.user.id)

@login_required
def Applyvacancy(request, pk):
    form = VacancyAppliedForm(request.POST or None)
    vacancys = Vacancy.objects.get(id=pk)
    jseekers=JobSeekerProfile.objects.get(user_id=request.user.id)
    user = request.user   
    vacancy = vacancys
    jseeker=jseekers
    jseeker = VacancyApply(vacancy=vacancy,user=user,jseeker=jseeker)
    jseeker.save()
    return redirect('VacancyStatus')  

class ViewApplicants(LoginRequiredMixin,generic.ListView):
    model= VacancyApply
    template_name='applicants.html'
    context_object_name='applicants'
    def get_queryset(self):
        return VacancyApply.objects.filter(vacancy__user=self.request.user.id)

@login_required
def AcceptApplicants(request, pk):
    applicants = VacancyApply.objects.get(id=pk)
    applicants.status = 2
    applicants.save()
    return redirect('applicants')

@login_required
def RejectApplicants(request, pk):
    applicants = VacancyApply.objects.get(id=pk)
    applicants.status = 3
    applicants.save()
    return redirect('applicants')

class RelatedJobs(LoginRequiredMixin,generic.ListView):
    model= Vacancy
    context_object_name = 'vacancys'
    template_name='jseeker-relatedjobs.html'

    def get_queryset(self):
        return(Vacancy.objects.filter(jobcategory=JobSeekerProfile.objects.get(user=self.request.user).interested_category))

class VacancyStatus(generic.ListView):
    model=VacancyApply
    context_object_name='vacancys'
    template_name='jseeker-status.html'
    def get_queryset(self):
        return(VacancyApply.objects.filter(user_id=self.request.user.id))

