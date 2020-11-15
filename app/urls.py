from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.Homepage.as_view(),name="home"),
    path("Emp_dash/<int:pk>",views.EmpDashboard.as_view(),name="dashboard"),
    path("Emp_dash/vacancy",views.Vacancy_create.as_view(),name="vacancy"),#Post vacancy
    path("Emp_dash/my-vacancy",views.My_vacancy.as_view(),name="my_vacancy"),
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path('Emp_dash/my-vacancy/update/<int:pk>',views.VacancyUpdateView.as_view(),name="update"),
    path('Emp_dash/my-vacancy/delete/<int:pk>',views.VacancyDeleteView.as_view(),name="delete"),
    path("search/",views.Search.as_view(),name="search"),
    path("jobseeker-dash/",views.JobSeekerDashboard.as_view(),name="Jobseeker_dashboard"),
    path("jobseeker-update/<int:pk>",views.UpdateJobSeeker,name="Jobseeker_update"),
    path("jobseeker-edu-info/<int:pk>/",views.EduInfo.as_view(),name="education-info"),
    path("jobseeker-add-edu",views.AddEduInfo.as_view(),name="add-edu-info"),
    path("jobseeker-update-info/<int:pk>",views.UpdateEduInfo.as_view(),name="edu-update-info"),
    path("jobseeker-skills",views.SkillSet.as_view(),name="skillset"),
    path("jobseeker-addskills/<int:pk>",views.AddSkillSet.as_view(),name="addskills"),
    path("jobseeker-deleteskills/<int:pk>",views.DeleteSkillSet.as_view(),name="deleteskills"),
    path("jobseeker-delete-edu-info/<int:pk>",views.DeleteEduInfo.as_view(),name="delete-edu-info"),
    path("jobseeker/training-info/<int:pk>",views.TrainingInfo.as_view(),name="training-info"),
    path("jobseeker/applyvacancy/<int:pk>",views.Applyvacancy,name="ApplyVacancy"),
    path("jobseeker/related-jobs/",views.RelatedJobs.as_view(),name="related-jobs"),
    path("Emp_dash/applicants/",views.ViewApplicants.as_view(),name="applicants"),
    path("Emp_dash/applicants/accept/<int:pk>/",views.AcceptApplicants,name="acceptapplicants"),
    path("Emp_dash/applicants/reject/<int:pk>/",views.RejectApplicants,name="rejectapplicants"),
    path("Emp-dash/status/Vacancy Status/",views.VacancyStatus.as_view(),name="VacancyStatus"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)