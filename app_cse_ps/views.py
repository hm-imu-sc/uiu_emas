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
    def action(self, request, **kwargs):
        self.redirect_url = "app_cse_ps:index"
        post_data = dict(**request.POST)

        project_title = post_data["project_title"][0]
        section_id =  post_data["course"][0]
        short_description = post_data["short_description"][0]
        project_members = post_data["project_members"][0]

        project_members = project_members.strip().split(',')

        self.database.query(f'INSERT INTO projects(title, section_id, short_description, trimester) VALUES ("{project_title}", "{section_id}", "{short_description}", "213")')
        project_id = self.database.query(f'SELECT id from projects where title = "{project_title}" and short_description = "{short_description}"')[0][0]
        for member in project_members:
            self.database.query(f'INSERT into project_members(project_id, student_id) VALUE ("{project_id}", "{member.strip()}")')
        return
