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
]
