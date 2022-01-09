from django.shortcuts import render
from my_modules.base_views import DBAction, DBRead
from django.views.generic import TemplateView
from my_modules.database import MySql
from django.http import HttpResponse
import json

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

class ArchiveProjects(TemplateView):
    template_name = "app_cse_ps/archieve_projects_page.html"
    database = MySql.db()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        projects = self.database.query("SELECT id, title, short_description FROM projects WHERE `status` = 1")
        context["data"] = []
        list = ['id', 'title', 'short_description', 'project_members']

        for tup in projects:
            members_id_tup = self.database.query(f"SELECT student_id FROM project_members WHERE project_id = {tup[0]}")
            members_id = []
            for member in members_id_tup:
                members_id.append(member[0])
            members_name = []
            for member in members_id:
                members_name.append(self.database.query(f"SELECT name FROM students WHERE student_id = {member}")[0][0])

            members_info = []
            for i in range(len(members_name)):
                members_info.append({'id' : members_id[i], 'name' : members_name[i]})

            context["data"].append({list[0]:tup[0],list[1]:tup[1],list[2]:tup[2], list[3]: members_info})
            print(context)
        return context

class ProjectRegistration(DBAction):
    def action(self, request, **kwargs):
        self.redirect_url = "app_cse_ps:index"
        post_data = dict(**request.POST)

        project_title = post_data["project_title"][0]
        section_id =  post_data["section"][0]
        short_description = post_data["short_description"][0]
        project_members = post_data["project_members"][0]

        project_members = project_members.strip().split(',')

        self.database.query(f'INSERT INTO projects(title, section_id, short_description, trimester) VALUES ("{project_title}", "{section_id}", "{short_description}", "213")')
        project_id = self.database.query(f'SELECT id from projects where title = "{project_title}" and short_description = "{short_description}"')[0][0]
        for member in project_members:
            self.database.query(f'INSERT into project_members(project_id, student_id) VALUE ("{project_id}", "{member.strip()}")')
        return

class CourseListPage(DBRead):

    template_name = "app_cse_ps/course_list_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = [
            # {
            #     "name": "Object Oriented Programming Laboratory",
            #     "code": "CSI TST",
            #     "num_sections": 4,
            #     "num_projects": 13
            # }
        ]

        courses = self.database.get_distinct("sections", ["course_code", "course_name"])

        for course in courses:
            num_sections = self.database.count("sections", {
                "course_code": course["course_code"],
            })

            section_ids = self.database.get("sections", ["id"], conditions = {
                "course_code": course["course_code"]
            })

            num_projects = self.database.count("projects", {
                "section_id": [section_id["id"] for section_id in section_ids]
            }, other_clauses=["and status=1"])

            context["courses"].append({
                "name": course["course_name"],
                "code": course["course_code"],
                "num_sections": num_sections,
                "num_projects": num_projects,
            })

        return context

class BoothListPage(DBRead):

    template_name = "app_cse_ps/booth_list_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_code = kwargs["course_code"]

        section_ids = self.database.get("sections", ["id"], {
            "course_code": course_code
        })

        projects = self.database.get("projects", ["id", "title", "short_description"], conditions={
            "section_id": [section_id["id"] for section_id in section_ids]
        }, other_clauses = ["and status=1"])

        for i in range(len(projects)):
            projects[i]["members"] = self.database.get("project_members", ["student_id"], {
                "project_id": projects[i]["id"]
            })

            for j in range(len(projects[i]["members"])):
                projects[i]["members"][j] = dict(**projects[i]["members"][j], **self.database.get("students", ["name"], {
                    "student_id": projects[i]["members"][j]["student_id"]
                })[0])

        context["projects"] = projects

        return context

def get_course_names(request):
    database = MySql.db()
    course_list = database.query("SELECT DISTINCT course_code, course_name FROM sections")
    context = {}
    context["data"] = []
    list = ['course_code','course_name']
    for tup in course_list:
        context["data"].append({list[0]:tup[0],list[1]:tup[1]})
    context = json.dumps(context)
    return HttpResponse(context)

def get_sections(request, course_code):
    database = MySql.db()
    section_list = database.query(f"SELECT id, name FROM sections WHERE course_code = '{course_code}'")
    context = {}
    context["data"] = []
    list = ['id','name']
    for tup in section_list:
        context["data"].append({list[0]:tup[0],list[1]:tup[1]})
    context = json.dumps(context)
    return HttpResponse(context)

def get_student(request, student_id):
    database = MySql.db()
    student_info = database.query(f"SELECT name, department FROM students WHERE student_id = '{student_id}'")
    context = {}
    if len(student_info) > 0:
        context["message"] = "OK"
    else:
        context["message"] = "NOT FOUND"

    context["data"] = []
    list = ['name', 'department']
    for tup in student_info:
        context["data"].append({list[0]:tup[0],list[1]:tup[1]})
    context = json.dumps(context)
    return HttpResponse(context)

def get_trimesters(request):
    database = MySql.db()
    trimesters = database.query("SELECT DISTINCT trimester FROM projects ORDER BY trimester ASC")
    context = {}
    context["data"] = []
    list = ['trimester']
    for tup in trimesters:
        context["data"].append({list[0]:tup[0]})
    context = json.dumps(context)
    return HttpResponse(context)

def get_filtered_archeive_projects(request, course_code, trimester):
    database = MySql.db()
    if (len(course_code)>0 and len(trimester)>0):
        projects = database.query(f"SELECT projects.id, projects.title, projects.short_description FROM projects JOIN sections ON projects.section_id = sections.id WHERE projects.status = 1 and projects.trimester = '{trimester}' and sections.course_code = '{course_code}'")
    elif len(course_code)>0:
        projects = database.query(f"SELECT projects.id, projects.title, projects.short_description FROM projects JOIN sections ON projects.section_id = sections.id WHERE projects.status = 1 and sections.course_code = '{course_code}'")
    elif len(trimester)>0:
        projects = database.query(f"SELECT projects.id, projects.title, projects.short_description FROM projects JOIN sections ON projects.section_id = sections.id WHERE projects.status = 1 and projects.trimester = '{trimester}'")
    else:
        projects = database.query(f"SELECT projects.id, projects.title, projects.short_description FROM projects JOIN sections ON projects.section_id = sections.id WHERE projects.status = 1")

    context = {}
    context["data"] = []
    list = ['id', 'title', 'short_description', 'project_members']

    for tup in projects:
        members_id_tup = database.query(f"SELECT student_id FROM project_members WHERE project_id = {tup[0]}")
        members_id = []
        for member in members_id_tup:
            members_id.append(member[0])
        members_name = []
        for member in members_id:
            members_name.append(database.query(f"SELECT name FROM students WHERE student_id = {member}")[0][0])

        members_info = []
        for i in range(len(members_name)):
            members_info.append({'id' : members_id[i], 'name' : members_name[i]})

        context["data"].append({list[0]:tup[0],list[1]:tup[1],list[2]:tup[2], list[3]: members_info})
    context = json.dumps(context)
    return HttpResponse(context)
