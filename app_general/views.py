from django.shortcuts import render
from my_modules.base_views import DBAction, DBRead
from django.views.generic import TemplateView
from my_modules.database import MySql
from django.core.files.storage import FileSystemStorage

# Create your views here.

class TestPage(DBRead):

    template_name = "app_general/test_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["test"] = "This is a Test Page"
        return context

class Test(DBAction):

    def action(self, request, **kwargs):
        self.redirect_url = "app_general:test_page"

        # print(request.FILES)

        files = dict(request.FILES)
        for f in files["f_1"]:
            print(f)

        # print(f)

        # fs = FileSystemStorage()
        # fs.save(f"reports/app_general/report.pdf", f)

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
    database = MySql.db()

    template_name = "app_general/project_details_page.html"

    def get_context_data(self, *args, **kwargs):
        context =  super().get_context_data(*args, **kwargs)
        project_id = kwargs["project_id"]

        #project details
        query = f'SELECT title, short_description, section_id FROM projects WHERE id = {int(project_id)}'
        project_details_tuple = self.database.query(query)
        project_title = project_details_tuple[0][0]
        project_short_description = project_details_tuple[0][1]
        section_id = project_details_tuple[0][2]

        #course details
        query = f'SELECT course_code, name, course_name FROM sections WHERE id = {int(section_id)}'
        course_details_tuple = self.database.query(query)
        course_code = course_details_tuple[0][0]
        section = course_details_tuple[0][1]
        course_name = course_details_tuple[0][2]

        #project members
        query = f'SELECT student_id FROM project_members WHERE project_id = {int(project_id)}'
        project_members_tuple = self.database.query(query)

        project_members_list = []

        for member in project_members_tuple:
            project_members_list.append(member[0])

        #project members details
        project_members_name_list = []
        for member in project_members_list:
            query = f'SELECT name FROM students WHERE student_id = {str(member)}'
            member_name = self.database.query(query)[0][0]
            project_members_name_list.append(member_name)

        context["id"] = project_id
        context["title"] = project_title
        context["description"] = project_short_description
        context["course"] = f'{course_code} ({section}): {course_name}'
        context["members"] = []

        for i in range(len(project_members_list)):
            context["members"].append({'id':project_members_list[i], 'name':project_members_name_list[i]})

        return context

class ProjectApprove(DBAction):
    def action(self, request, **kwargs):
        self.redirect_url = "app_general:teacher_dashboard_page"
        project_id = kwargs["project_id"]
        query = f'UPDATE projects SET status = 1 WHERE id = {int(project_id)}'
        self.database.query(query)
        return

class BoothSetupPage(TemplateView):

    template_name = 'app_general/booth_setup_page.html'
    database = MySql.db()

    def get_context_data(self,*args,**kwargs):
        self.boothid=kwargs['project_id']
        self.boothid=1 # delete this line
        context = super().get_context_data(*args, **kwargs)
        booth_details = self.database.query(f'SELECT id,title,short_description FROM projects WHERE id={self.boothid}')
        context['booth_details']={'id':booth_details[0][0],'title':booth_details[0][1],'short_description':booth_details[0][2]}
        return context

class BoothSetup(DBAction):
    def action(self, request, **kwargs):
        proj_id=request.POST['proj_id']
        self.redirect_url = f"app_general:index"

        #intro video upload
        intro_video = request.FILES['intro_video']
        fs=FileSystemStorage()
        intro_path=f'video/app_general/{proj_id}_intro_video.mp4'
        fs.save(intro_path,intro_video)

        #demo video
        demo_videos = request.FILES.getlist('demo_videos')
        files = dict(request.FILES)
        video_paths=[]
        i=0
        print(len(demo_videos))
        for video in demo_videos:
            video_path=f'video/app_general/{proj_id}_demo_video{i}.mp4'
            fs.save(video_path,video)
            video_paths.append(video_path)
            i+=1

        #report
        report = request.FILES['report']
        report_path=f'pdf/app_general/{proj_id}_report.pdf'
        fs.save(report_path, report)
        self.database.query(f'UPDATE projects SET intro_video="{intro_path}",report="{report_path}" WHERE id="{proj_id}"')

        for path in video_paths:
            self.database.query(f'INSERT INTO project_videos (project_id,path) VALUES ("{proj_id}","{path}")')

        return
