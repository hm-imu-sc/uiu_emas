from django.shortcuts import render
from my_modules.base_views import DBAction
from django.views.generic import TemplateView
from my_modules.database import MySql
# Create your views here.

class Index(TemplateView):
    template_name = "app_cse_ps/index.html"

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs)

class ProjectRegistrationPage(TemplateView):
    template_name = "app_cse_ps/project_registration_page.html"
    database = MySql.db()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        unique_sections_tuple = self.database.query("SELECT DISTINCT id, course_code, course_name, name FROM sections")
        context["data"] = []
        list = ['id', 'course_code','course_name','name']
        for tup in unique_sections_tuple:
            context["data"].append({list[0]:tup[0],list[1]:tup[1],list[2]:tup[2],list[3]:tup[3]})
        return context

class ProjectRegistration(DBAction):
    pass
