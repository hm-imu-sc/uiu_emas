from django.conf import settings
from django.urls import path
from . import views

app_name = "app_cse_ps"

urlpatterns = [
    path("index/", views.Index.as_view(), name="index"),
    path("project_registration_page/",views.ProjectRegistrationPage.as_view(), name="project_registration_page"),
    path("project_registration/",views.ProjectRegistration.as_view(), name="project_registration"),
    path("course_list_page/", views.CourseListPage.as_view(), name="course_list_page"),
    path("booth_list_page/<course_code>", views.BoothListPage.as_view(), name="booth_list_page"),
    path("get_course_names/", views.get_course_names, name="get_course_names"),
    path("get_sections/<course_code>", views.get_sections, name="get_sections"),
    path("get_student/<student_id>", views.get_student, name="get_student"),
    path("archieve_projects/", views.ArchiveProjects.as_view(), name="archieve_projects"),
    path("get_trimesters/", views.get_trimesters, name="get_trimesters"),
    path("get_filtered_archeive_projects/<course_code>/<trimester>", views.get_filtered_archeive_projects, name="get_filtered_archeive_projects"),
    path("project_booth_page/<project_id>/", views.ProjectBoothPage.as_view(), name="project_booth_page"),    
    path("comment_loader/<project_id>/<already_loaded>/", views.CommentLoader.as_view(), name="comment_loader"),
]
