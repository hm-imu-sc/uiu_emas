from django.urls import path
from . import views

app_name = "app_general"

urlpatterns = [
    path("index/", views.Index.as_view(), name="index"),
    path("student_registration_page/", views.StudentRegistrationPage.as_view(), name="student_registration_page"),
    path("student_registration/", views.StudentRegistration.as_view(), name="student_registration"),
    path("login_page/", views.LoginPage.as_view(), name="login_page"),
]