from django.shortcuts import render
from my_modules.base_views import DBAction
from django.views.generic import TemplateView

from django.shortcuts import render
from my_modules.base_views import DBAction, DBRead
from django.views.generic import TemplateView
from my_modules.database import MySql
from django.http import HttpResponse
import json


# Create your views here.

class Index(TemplateView):
    template_name = "app_club_ff/index.html"

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs)


class FestRegistrationPage(TemplateView):
    template_name = "app_club_ff/fest_registration_page.html"
    database = MySql.db()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        student_id = kwargs["student_id"]
        already_exist = self.database.query(f"SELECT * FROM cff_registrations WHERE student_id = '{student_id}'")
        if len(already_exist) != 0:
            self.template_name = "app_club_ff/fest_already_registered.html"
            return context

        student = self.database.query(
            f"SELECT student_id, name, uiu_email FROM students WHERE student_id = '{student_id}'")
        context["data"] = []
        list = ['student_id', 'name', 'uiu_email']
        for tup in student:
            context["data"].append({list[0]: tup[0], list[1]: tup[1], list[2]: tup[2]})
        return context


class FestRegistration(DBAction):
    def action(self, request, **kwargs):
        self.redirect_url = "app_club_ff:index"
        post_data = dict(**request.POST)
        print('YES')
        student_id = post_data["student_id"][0]
        club_id = post_data["club"][0]
        tshirt_size = post_data["tshirt_size"][0]

        self.database.query(
            f"INSERT INTO cff_registrations (student_id,club_id, t_shirt_size) VALUES ('{student_id}','{club_id}','{tshirt_size}')")
        return


def get_club_names(request):
    database = MySql.db()
    club_list = database.query("SELECT club_id, name FROM clubs")
    context = {}
    context["data"] = []
    list = ['club_id', 'club_name']
    for tup in club_list:
        context["data"].append({list[0]: tup[0], list[1]: tup[1]})
    context = json.dumps(context)
    return HttpResponse(context)


def get_cff_years(request):
    database = MySql.db()
    years = database.query("SELECT DISTINCT year(time_created) FROM booths")
    context = {}
    context["data"] = []
    list = ['year']
    for tup in years:
        context["data"].append({list[0]: tup[0]})
    print(context["data"])
    context = json.dumps(context)
    return HttpResponse(context)


class FestFeed(DBRead):
    template_name = "app_club_ff/fest_feed_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clubs"] = self.get_club_names()
        context["sorting_criterias"] = [
            {"value": "desc", "option": "Newest"},
            {"value": "asc", "option": "Oldest"}
        ]
        context["feed_posts"] = self.get_feed_posts()
        context["length"] = len(context["feed_posts"])
        return context

    def get_club_names(self):
        database = MySql.db()
        club_name = database.get("clubs")
        return club_name

    def get_feed_posts(self):
        database = MySql.db()
        feed_posts = database.get("feed_posts", other_clauses=[
            "order by time_created asc",
            "limit 5"
        ])
        return feed_posts


class PostProcessor(DBRead):
    template_name = "app_club_ff/post_processor.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        offset = int(kwargs["offset"])
        club_id = kwargs["club_id"]
        criteria = kwargs["criteria"]

        context["feed_posts"] = self.get_feed_posts(offset, club_id, criteria)
        context["length"] = len(context["feed_posts"]) + offset
        # print(context["posts"])
        print(context["length"])
        return context

    def get_feed_posts(self, offset, club_id, criteria):
        # database = MySql.db()
        conditions = None

        if club_id != "all":
            conditions = {
                "club_id": club_id
            }
        feed_posts = self.database.get("feed_posts", conditions=conditions, other_clauses=[
            f"order by time_created {criteria}",
            "limit 5",
            f"offset {offset}" if offset != -1 else "",
        ])
        return feed_posts


# def get_filtered_archive_cff_booths(request, course_code, trimester):
#     database = MySql.db()
#     print(course_code)
#     print(trimester)
#     if course_code!='NULL' :
#         projects = database.query(f"SELECT projects.id, projects.title, projects.short_description FROM projects JOIN sections ON projects.section_id = sections.id WHERE projects.status = 1 and projects.trimester = '{trimester}' and sections.course_code = '{course_code}'")
#     elif course_code!='NULL':
#         projects = database.query(f"SELECT projects.id, projects.title, projects.short_description FROM projects JOIN sections ON projects.section_id = sections.id WHERE projects.status = 1 and sections.course_code = '{course_code}'")
#     elif trimester!='NULL':
#         projects = database.query(f"SELECT projects.id, projects.title, projects.short_description FROM projects JOIN sections ON projects.section_id = sections.id WHERE projects.status = 1 and projects.trimester = '{trimester}'")
#     else:
#         projects = database.query(f"SELECT projects.id, projects.title, projects.short_description FROM projects JOIN sections ON projects.section_id = sections.id WHERE projects.status = 1")
#
#     context = {}
#     context["data"] = []
#     list = ['id', 'title', 'short_description', 'project_members']
#
#     for tup in projects:
#         members_id_tup = database.query(f"SELECT student_id FROM project_members WHERE project_id = {tup[0]}")
#         members_id = []
#         for member in members_id_tup:
#             members_id.append(member[0])
#         members_name = []
#         for member in members_id:
#             members_name.append(database.query(f"SELECT name FROM students WHERE student_id = {member}")[0][0])
#
#         members_info = []
#         for i in range(len(members_name)):
#             members_info.append({'id' : members_id[i], 'name' : members_name[i]})
#
#         context["data"].append({list[0]:tup[0],list[1]:tup[1],list[2]:tup[2], list[3]: members_info})
#     context = json.dumps(context)
#     return HttpResponse(context)


class ArchiveCffBooths(TemplateView):
    template_name = "app_club_ff/archive_cff_booths_page.html"
    database = MySql.db()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        booths = self.database.query(
            "SELECT id, time_created, club_id, club_description FROM booths WHERE `status` = 1")

        context["data"] = []
        club_name_list = []
        list = ['id', 'time_created', 'club_id', 'club_description', 'club_name']

        for tup in booths:
            c_name = self.database.query(f"SELECT name FROM clubs WHERE id = {tup[2]}")
            c_name = c_name[0]
            context["data"].append(
                {list[0]: tup[0], list[1]: tup[1], list[2]: tup[2], list[3]: tup[3], list[4]: c_name[0]})
        return context
