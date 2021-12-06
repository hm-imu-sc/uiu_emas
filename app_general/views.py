from django.shortcuts import render
from my_modules.base_views import DBAction
from django.views.generic import TemplateView
from my_modules.database import MySql

# Create your views here.

class Index(TemplateView):

    template_name = "app_general/index.html"

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs)

class StudentRegistrationPage(TemplateView):

    template_name = "app_general/student_registration_page.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context["date"] = {
            "days": [i for i in range(32)[1:]],
            "months": [i for i in range(13)[1:]],
            "years": [i for i in range(2022)[1990:][::-1]]
        }

        return context

class StudentRegistration(DBAction):    

    def action(self, request, **kwargs):
        self.redirect_url = "app_general:login_page"
        
        post_data = dict(**request.POST)

        student_id = post_data["student_id"][0]
        name = post_data["name"][0]
        email = post_data["email"][0]
        phone_number = post_data["phone_number"][0]
        department = post_data["department"][0]
        password = post_data["password"][0]
        dob = {
            "day": post_data["day"][0],
            "month": post_data["month"][0],
            "year": post_data["year"][0],
        }
        retype_password = post_data["retype_password"][0]

        self.database.insert("students", [
            {
                "student_id": student_id,
                "name": name,
                "uiu_email": email,
                "phone_number": phone_number,
                "department": department,
                "password_hash": password,
                "photo": "null",
                "dob": f"{dob['year']}-{dob['month']}-{dob['day']}"
            }
        ])

        # return super().action(request, **kwargs)

class LoginPage(TemplateView):

    template_name = "app_general/login_page.html"

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs)

class TeacherDashboardPage(TemplateView):
    database = MySql.db()

    template_name = "app_general/teacher_dashboard_page.html"

    def get_context_data(self, *args, **kwargs):
        context =  super().get_context_data(*args, **kwargs)

        teacher_id = 'SS'
        sections = self.database.get('sections', conditions = {
            "teacher_id": teacher_id
        })
        conditions = "("

        for i in range(len(sections)):
            conditions += f" section_id = {sections[i]['id']} "
            if i + 1 < len(sections):
                conditions += "or"

        conditions += f") and status = 0 "

        projects = self.database.fetch_dict("projects", self.database.query(f"select * from projects where {conditions}"))

        context['projects'] = projects

        teacher_name = self.database.get('teachers', conditions = {"employee_id": teacher_id})[0]["name"]

        context['teacher_name'] = teacher_name
        
        return context

class ProjectDetailsPage(TemplateView):
    pass

class BoothSetupPage(TemplateView):

    template_name = 'app_general/booth_setup_page.html'
    database = MySql.db()

    def get_context_data(self,*args,**kwargs):
        self.boothid=super().get_context_data() # insert boothid here
        context = super().get_context_data(*args, **kwargs)
        booth_details = self.database.query(f'SELECT id,title,section_id,short_description FROM projects WHERE ')




