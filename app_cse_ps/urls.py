from django.conf import settings
from django.urls import path
from . import views

app_name = "app_cse_ps"

urlpatterns = [
    path("index/", views.Index.as_view(), name="index"),
    path("project_registration_page/",views.ProjectRegistrationPage.as_view(), name="project_registration_page"),
    path("project_registration/",views.ProjectRegistration.as_view(), name="project_registration"),
]
