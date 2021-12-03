from django.shortcuts import render
from my_modules.base_views import DBAction
from django.views.generic import TemplateView

# Create your views here.

class Index(TemplateView):

    template_name = "app_general/index.html"

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs)

class StudentRegistrationPage(TemplateView):

    template_name = "app_general/student_registration.html"

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs)

class LoginPage(TemplateView):

    template_name = "app_general/login_page.html"

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs)