from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "app_general"

urlpatterns = [
    path("index/", views.Index.as_view(), name="index"),
    path("student_registration_page/", views.StudentRegistrationPage.as_view(), name="student_registration_page"),
    path("student_registration/", views.StudentRegistration.as_view(), name="student_registration"),
    path("login_page/", views.LoginPage.as_view(), name="login_page"),
    path("teacher_dashboard_page/", views.TeacherDashboardPage.as_view(), name="teacher_dashboard_page"),
    path("student_dashboard_page/", views.StudentDashboardPage.as_view(), name="student_dashboard_page"),
    path("project_details_page/<project_id>/", views.ProjectDetailsPage.as_view(), name= "project_details_page"),
    path("project_approve/<project_id>/", views.ProjectApprove.as_view(), name="project_approve"),
    path("booth_setup_page/<project_id>/",views.BoothSetupPage.as_view(), name="booth_setup_page"),
    path("booth_setup/",views.BoothSetup.as_view(), name="booth_setup"),
    # path("test_page/", views.TestPage.as_view(), name="test_page"),
    path("test_page/", views.TestPage.respond, name="test_page"),
    path("test/<len>/", views.Test.as_view(), name="test"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
