from django.shortcuts import render, redirect
from my_modules.base_views import DBAction, DBRead
from django.views.generic import TemplateView
from my_modules.database import MySql
from django.core.files.storage import FileSystemStorage
from datetime import datetime, timedelta
import hashlib

# Create your views here.

class TestPage(DBRead):
    template_name = "app_general/test_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["test"] = "This is a Test Page"
        return context


class Test(DBRead):

    template_name = "app_general/test.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["len"] = [l for l in range(int(kwargs["len"]))]
        context["data"] = {
            "info1": "290",
            "info2": "076",
            "info3": "062",
        }
        return context
    

class Index(DBRead):
    template_name = "app_general/index.html"

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs)


class StudentRegistrationPage(DBRead):
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


class LoginPage(DBRead):
    template_name = "app_general/login_page.html"

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs)


class Login(DBAction):
    
    def action(self, request, **kwargs):

        try:
            user = request.POST["user"]
            password = request.POST["password"]
        except Exception:
            self.redirect_url = "app_general:login_page"
            return

        user_domains = {
            "student": ["student_id", "uiu_email"],
            "teacher": ["employee_id", "uiu_email"]
        }

        user_data = None
        user_domain = None

        for key in user_domains.keys():
            
            user_data = self.database.get(f"{key}s", conditions={
                user_domains[key][0]: user,
                user_domains[key][1]: user,
            }, condition_connector = "or")
            
            if len(user_data) == 1:
                user_data = user_data[0]
                user_domain = key
                break

        if user_data is None or not self.verify_password(user_data, password):
            self.redirect_url = "app_general:login_page"
            return

        user_id = user_data[user_domains[user_domain][0]]
        # password_hash = user_data["password_hash"]

        # request.session["user"] = {
        #     "id": user_id,
        #     "domain": {
        #         "name": user_domain,
        #         "field": user_domains[user_domain][0]
        #     },
        #     "identification_hash": hashlib.sha256(f"{user_id}({password_hash})".encode("ASCII")).hexdigest()
        # }

        request.session["user"] = {
            "login_status": True,
            "id": user_id,
            "domain": user_domain
        }

        request.session.set_expiry(24 * 3600)

        self.redirect_url = f"app_general:{user_domain}_dashboard_page"

    def verify_password(self, user, password):
        given = hashlib.sha256(password.encode("ASCII")).hexdigest()
        return user["password_hash"] == given


class Logout(DBAction):
    
    def action(self, request, **kwargs):
        self.redirect_url = "app_general:login_page"
        del request.session["user"]


class TeacherDashboardPage(DBRead):
    database = MySql.db()

    template_name = "app_general/teacher_dashboard_page.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        teacher_id = kwargs["request"].session["user"]["id"]
        sections = self.database.get('sections', conditions={
            "teacher_id": teacher_id
        })

        section_ids = [sections[i]['id'] for i in range(len(sections))]
        projects = []

        if len(section_ids) > 0:
            projects = self.database.get("projects", conditions={
                "section_id": section_ids,
                "status": 0
            })

        context['projects'] = projects

        teacher_name = self.database.get('teachers', conditions={"employee_id": teacher_id})[0]["name"]

        context['teacher_name'] = teacher_name

        return context


class StudentDashboardPage(DBRead):
    database = MySql.db()

    template_name = "app_general/student_dashboard_page.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        student_id = kwargs["request"].session["user"]["id"]

        project_ids = self.database.get("project_members", ["project_id"], conditions = {"student_id": student_id})
        context['projects'] = []

        for project_id in project_ids:
            projects = self.database.get("projects", conditions = {
                "id": project_id["project_id"]
            })

            if len(projects) > 0:
                context['projects'].append(projects[0])

        project_id = self.database.get('project_members', conditions={"student_id": student_id})[0]["project_id"]

        context['project_id'] = project_id
        context["student_id"] = student_id

        query = f'SELECT title, status FROM projects WHERE id = {int(project_id)}'
        project_details = self.database.query(query)

        project_status = project_details[0][1]
        project_title = project_details[0][0]

        query = f'SELECT name FROM students WHERE student_id = {student_id}'
        student_details = self.database.query(query)
        student_name = student_details[0][0]

        context["name"] = student_name

        return context


class ProjectDetailsPage(DBRead):
    database = MySql.db()

    template_name = "app_general/project_details_page.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        project_id = kwargs["project_id"]

        # project details
        query = f'SELECT title, short_description, section_id FROM projects WHERE id = {int(project_id)}'
        project_details_tuple = self.database.query(query)
        project_title = project_details_tuple[0][0]
        project_short_description = project_details_tuple[0][1]
        section_id = project_details_tuple[0][2]

        # course details
        query = f'SELECT course_code, name, course_name FROM sections WHERE id = {int(section_id)}'
        course_details_tuple = self.database.query(query)
        course_code = course_details_tuple[0][0]
        section = course_details_tuple[0][1]
        course_name = course_details_tuple[0][2]

        # project members
        query = f'SELECT student_id FROM project_members WHERE project_id = {int(project_id)}'
        project_members_tuple = self.database.query(query)

        project_members_list = []

        for member in project_members_tuple:
            project_members_list.append(member[0])

        # project members details
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
            context["members"].append({'id': project_members_list[i], 'name': project_members_name_list[i]})

        return context


class ProjectApprove(DBAction):
    def action(self, request, **kwargs):
        self.redirect_url = "app_general:teacher_dashboard_page"
        project_id = kwargs["project_id"]
        query = f'UPDATE projects SET status = 1 WHERE id = {int(project_id)}'
        self.database.query(query)
        return


class BoothSetupPage(DBRead):
    template_name = 'app_general/booth_setup_page.html'
    database = MySql.db()

    def get_context_data(self, *args, **kwargs):
        self.boothid = kwargs['project_id']
        # self.boothid = 1  # delete this line
        context = super().get_context_data(*args, **kwargs)
        booth_details = self.database.query(f'SELECT id,title,short_description FROM projects WHERE id={self.boothid}')
        context['booth_details'] = {'id': booth_details[0][0], 'title': booth_details[0][1],
                                    'short_description': booth_details[0][2]}
        return context


class BoothSetup(DBAction):
    def action(self, request, **kwargs):
        proj_id = request.POST['proj_id']
        self.redirect_url = f"app_general:index"

        # intro video upload
        intro_video = request.FILES['intro_video']
        fs = FileSystemStorage()
        intro_path = f'video/app_general/{proj_id}_intro_video.mp4'
        fs.save(intro_path, intro_video)

        # demo video
        demo_videos = request.FILES.getlist('demo_videos')
        files = dict(request.FILES)
        video_paths = []
        i = 0
        print(len(demo_videos))
        for video in demo_videos:
            video_path = f'video/app_general/{proj_id}_demo_video{i}.mp4'
            fs.save(video_path, video)
            video_paths.append(video_path)
            i += 1

        # report
        report = request.FILES['report']
        report_path = f'pdf/app_general/{proj_id}_report.pdf'
        fs.save(report_path, report)
        self.database.query(
            f'UPDATE projects SET intro_video="{intro_path}",report="{report_path}" WHERE id="{proj_id}"')

        for path in video_paths:
            self.database.query(f'INSERT INTO project_videos (project_id,path) VALUES ("{proj_id}","{path}")')

        return
