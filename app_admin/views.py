from django.shortcuts import render
from my_modules.base_views import DBAction,DBRead
from django.views.generic import TemplateView
from my_modules.database import MySql
from django.http import HttpResponse
import json

# Create your views here.

class Index(DBRead):
    template_name = "app_admin/index.html"

    def get_context_data(self, request,  *args, **kwargs):
        return {}

# class BoothSetupPage(DBRead):
#     template_name = 'app_general/booth_setup_page.html'
#     database = MySql.db()
#
#     def get_context_data(self, request,  *args, **kwargs):
#         self.boothid = kwargs['project_id']
#         # self.boothid = 1  # delete this line
#         context = {}
#         booth_details = self.database.query(f'SELECT id,title,short_description FROM projects WHERE id={self.boothid}')
#         context['booth_details'] = {'id': booth_details[0][0], 'title': booth_details[0][1],
#                                     'short_description': booth_details[0][2]}
#         return context

class PrizeGivingPage(DBRead):
    template_name = "app_admin/prize_giving_page.html"

    def get_context_data(self, *args ,**kwargs):
        context = {}
        trimesters = self.database.query(f'SELECT DISTINCT trimester FROM sections')
        context['trimesters'] = list(trimesters[0])
        print(context)
        return context

def get_course_by_trimester(request,**kwargs):

    print(kwargs)
    database = MySql.db()
    context = {}
    courses = database.query(f'SELECT DISTINCT course_code,course_name FROM sections WHERE trimester={kwargs["trimester"]}')
    if len(courses) > 0:
        context["message"] = "OK"
    else:
        context["message"] = "NOT FOUND"

    context["data"] = []
    list = ['course_code', 'course_name']
    for tup in courses:
        context["data"].append({list[0]: tup[0], list[1]: tup[1]})
    context = json.dumps(context)
    return HttpResponse(context)

def get_projects_by_course_code(request,**kwargs):
    #print("efwfwgwrgwrgrwgwrgwrrgwrgwgrwgwrgwrg")
    #print(kwargs)
    database = MySql.db()
    context = {}
    section_ids = database.query(f'SELECT id FROM sections WHERE course_code="{kwargs["course_code"]}"')
    section_ids =[ s[0] for s in section_ids]
    ids = ""
    for temp in section_ids:
        ids += str(temp) + ","
    ids = ids[:-1]
    #project_ids = database.query(f'SELECT id,title FROM projects WHERE section_id IN ({ids})')
    project_ids = database.query(f'SELECT id,title FROM projects WHERE EXISTS (SELECT project_id FROM prizes where projects.id!=prizes.project_id) AND section_id IN ({ids})')

    if len(project_ids) > 0:
        context["message"] = "OK"
    else:
        context["message"] = "NOT FOUND"

    context["data"] = []
    list = ['project_id','title']
    for tup in project_ids:
        context["data"].append({list[0]: tup[0], list[1]: tup[1]})
    context = json.dumps(context)
    return HttpResponse(context)

class GiveAward(DBAction):
    def action(self, request, **kwargs):
        self.redirect_url = f"app_admin:prize_giving_page"
        project_id = request.POST["projects"]
        student_ids = self.database.query(f'SELECT student_id FROM project_members WHERE project_id = {project_id}')
        student_ids = [s[0] for s in student_ids]
        prize=request.POST["prize"]
        for id in student_ids:
            self.database.query(f'INSERT INTO prizes (project_id,student_id,prize) VALUES ("{project_id}","{id}","{prize}")')
        return



