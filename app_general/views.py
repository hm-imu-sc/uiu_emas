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

    def get_context_data(self, request, *args, **kwargs):
        return {
            "user": "student"
        }


class Test(DBRead):

    template_name = "app_general/test.html"

    def get_context_data(self, request, *args, **kwargs):
        context = {}
        context["len"] = [l for l in range(int(kwargs["len"]))]
        context["data"] = {
            "info1": "290",
            "info2": "076",
            "info3": "062",
        }
        return context
    

class Index(DBRead):
    template_name = "app_general/index.html"

    def get_context_data(self, request,  *args, **kwargs):
        return {}


class StudentRegistrationPage(DBRead):
    template_name = "app_general/student_registration_page.html"

    def get_context_data(self, request,  *args, **kwargs):
        context = {}

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
                "password_hash": hashlib.sha256(password.encode("ASCII")).hexdigest(),
                "photo": "null",
                "dob": f"{dob['year']}-{dob['month']}-{dob['day']}"
            }
        ])

        # return super().action(request, **kwargs)


class LoginPage(DBRead):
    template_name = "app_general/login_page.html"

    def get_context_data(self, request,  *args, **kwargs):
        # return {}
        return {}


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

        request.session["user"] = {
            "login_status": True,
            "id": user_id,
            "domain": user_domain
        }

        request.session.set_expiry(24 * 3600)

        self.redirect_url = f"app_general:{user_domain}_dashboard_page"

    def verify_password(self, user, password):

        if len(user) == 0:
            return False

        given = hashlib.sha256(password.encode("ASCII")).hexdigest()
        # print(given)
        # print(user)
        return user["password_hash"] == given


class Logout(DBAction):
    
    def action(self, request, **kwargs):
        self.redirect_url = "app_general:login_page"
        del request.session["user"]


class TeacherDashboardPage(DBRead):
    database = MySql.db()

    template_name = "app_general/teacher_dashboard_page.html"

    def get_context_data(self, request,  *args, **kwargs):
        context = {}

        teacher_id = request.session["user"]["id"]
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
    template_name = "app_general/student_dashboard_page.html"

    def get_context_data(self, request,  *args, **kwargs):
        context = {}

        student_id = request.session["user"]["id"]

        project_ids = self.database.get("project_members", ["project_id"], conditions = {"student_id": student_id})
        context['projects'] = []

        for project_id in project_ids:
            project = self.database.get("projects", ["id", "title", "section_id"], conditions = {
                "id": project_id["project_id"],
                "status": 1
            })[0]

            project["course"] = self.database.get("sections", ["name", "course_code", "course_name"], {"id": project["section_id"]})[0]
            project["team"] = [
                team_member["student_id"]
                for team_member in self.database.get("project_members", ["student_id"], conditions = project_id)
            ]

            context['projects'].append(project)

        context["student"] = {
            "id": student_id,
            **self.database.get("students", ["name", "department"], {"student_id": student_id})[0],
        }

        return context


class ProjectProcessor(DBRead):
    template_name = "app_general/project_processor.html"

    def get_context_data(self, request,  *args, **kwargs):

        context = {}

        student_id = request.session["user"]["id"]
        project_status = kwargs["project_status"]

        project_ids = self.database.get("project_members", ["project_id"], conditions = {"student_id": student_id})
        context['projects'] = []

        for project_id in project_ids:
            project = self.database.get("projects", ["id", "title", "section_id"], conditions = {
                "id": project_id["project_id"],
                "status": project_status
            })

            if len(project) == 0:
                continue
            
            project = project[0]

            project["course"] = self.database.get("sections", ["name", "course_code", "course_name"], {"id": project["section_id"]})[0]
            project["team"] = [
                team_member["student_id"]
                for team_member in self.database.get("project_members", ["student_id"], conditions = project_id)
            ]

            project["status"] = project_status

            context['projects'].append(project)

        context["student"] = {
            "id": student_id,
            **self.database.get("students", ["name", "department"], {"student_id": student_id})[0],
        }

        return context
    

class ProjectDetailsPage(DBRead):
    database = MySql.db()

    template_name = "app_general/project_details_page.html"

    def get_context_data(self, request,  *args, **kwargs):
        context = {}
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

    def get_context_data(self, request,  *args, **kwargs):
        self.boothid = kwargs['project_id']
        # self.boothid = 1  # delete this line
        context = {}
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
        name = intro_video.name
        ext = name.split('.')[-1]
        intro_path = f'projects-{proj_id}-intro_video.{ext}'
        fs.save(intro_path, intro_video)

        # demo video
        demo_videos = request.FILES.getlist('demo_videos')
        files = dict(request.FILES)
        video_paths = []
        i = 0
        print(len(demo_videos))

        max_project_videos_id = self.database.query("SELECT MAX(id) AS id FROM project_videos")
        max_project_videos_id = max_project_videos_id[0][0]

        for video in demo_videos:
            max_project_videos_id+=1
            name=video.name
            ext=name.split('.')[-1]
            print(ext)
            video_path = f'project_videos-{max_project_videos_id}-path.{ext}'
            fs.save(video_path, video)
            video_paths.append(video_path)
            i += 1

        print(type(demo_videos[0]))
        print(demo_videos[0])

        # report
        report = request.FILES['report']
        name = report.name
        ext = name.split('.')[-1]
        report_path = f'projects-{proj_id}-report.{ext}'
        fs.save(report_path, report)



        self.database.query(
            f'UPDATE projects SET intro_video="{intro_path}",report="{report_path}" WHERE id="{proj_id}"')



        for path in video_paths:
            self.database.query(f'INSERT INTO project_videos (project_id,path) VALUES ("{proj_id}","{path}")')

        return
