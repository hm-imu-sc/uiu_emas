from django.shortcuts import render
from my_modules.base_views import DBAction,DBRead
from django.views.generic import TemplateView
from my_modules.database import MySql
from django.http import HttpResponse
import json

# Create your views here.

class Index(TemplateView):
    template_name = "app_admin/index.html"

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs)

# class BoothSetupPage(TemplateView):
#     template_name = 'app_general/booth_setup_page.html'
#     database = MySql.db()
#
#     def get_context_data(self, *args, **kwargs):
#         self.boothid = kwargs['project_id']
#         # self.boothid = 1  # delete this line
#         context = super().get_context_data(*args, **kwargs)
#         booth_details = self.database.query(f'SELECT id,title,short_description FROM projects WHERE id={self.boothid}')
#         context['booth_details'] = {'id': booth_details[0][0], 'title': booth_details[0][1],
#                                     'short_description': booth_details[0][2]}
#         return context

class PrizeGivingPage(DBRead):
    template_name = "app_admin/prize_giving_page.html"

    def get_context_data(self, *args ,**kwargs):
        context = super().get_context_data(*args, **kwargs)
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

def get_projects_by_section_id(request,**kwargs):
    print("efwfwgwrgwrgrwgwrgwrrgwrgwgrwgwrgwrg")
    print(kwargs)
    database = MySql.db()
    context = {}
    section_ids = database.query(f'SELECT id FROM sections WHERE course_code="{kwargs["course_code"]}"')
    print(section_ids)
    section_ids =[ s[0] for s in section_ids]
    print(section_ids)
    project_ids = database.query(f'SELECT id FROM sections WHERE course_code="{kwargs["course_code"]}"')
    # if len(courses) > 0:
    #     context["message"] = "OK"
    # else:
    #     context["message"] = "NOT FOUND"
    #
    # context["data"] = []
    # list = ['project_id','title']
    # for tup in courses:
    #     context["data"].append({list[0]: tup[0], list[1]: tup[1], list[3]: tup[3]})
    # context = json.dumps(context)
    return HttpResponse(context)

