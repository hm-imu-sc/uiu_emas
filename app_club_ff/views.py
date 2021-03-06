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

class Index(DBRead):
    template_name = "app_club_ff/index.html"


class FestRegistrationPage(DBRead):
    template_name = "app_club_ff/fest_registration_page.html"
    database = MySql.db()

    def get_context_data(self, request,  *args, **kwargs):
        context = {}
        student_id = request.session["user"]["id"]
        print(student_id)
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


class FestFeed(DBRead):
    template_name = "app_club_ff/fest_feed_page.html"

    def get_context_data(self, request, *args, **kwargs):
        context = {}
        context["clubs"] = self.get_club_names()
        context["sorting_criterias"] = [
            {"value": "desc", "option": "Newest"},
            {"value": "asc", "option": "Oldest"}
        ]
        context["feed_posts"] = self.get_feed_posts()
        context["length"] = len(context["feed_posts"])
        return context

    def get_club_names(self):
        club_name = self.database.get("clubs")
        return club_name

    def get_feed_posts(self):
        feed_posts = self.database.get("feed_posts", other_clauses=[
            "order by time_created desc",
            "limit 5"
        ])

        for i in range(len(feed_posts)):
            club_name = self.database.get("clubs", ["name"], {"id": feed_posts[i]["club_id"]})[0]["name"]
            feed_posts[i]["club_name"] = club_name

        return feed_posts


class PostProcessor(DBRead):
    template_name = "app_club_ff/post_processor.html"

    def get_context_data(self, request, *args, **kwargs):
        context = {}

        offset = int(kwargs["offset"])
        club_id = kwargs["club_id"]
        criteria = kwargs["criteria"]

        context["feed_posts"] = self.get_feed_posts(offset, club_id, criteria)
        context["length"] = len(context["feed_posts"]) + offset
        return context

    def get_feed_posts(self, offset, club_id, criteria):
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

        for i in range(len(feed_posts)):
            club_name = self.database.get("clubs", ["name"], {"id": feed_posts[i]["club_id"]})[0]["name"]
            feed_posts[i]["club_name"] = club_name

        return feed_posts


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


def get_filtered_cff(request, club_name, year):
    database = MySql.db()
    print(club_name)
    print(year)

    if club_name != 'NULL' and year == 'NULL':
        booths = database.query(
            f"SELECT booths.id, YEAR(booths.time_created), booths.club_id, booths.club_description, clubs.name FROM booths JOIN clubs ON booths.club_id = clubs.club_id WHERE booths.status = 1 and clubs.name = '{club_name}' ")
    elif year != 'NULL' and club_name == 'NULL':
        booths = database.query(
            f"SELECT booths.id, YEAR(booths.time_created), booths.club_id, booths.club_description, clubs.name FROM booths JOIN clubs ON booths.club_id = clubs.club_id WHERE booths.status = 1 and YEAR(booths.time_created) = '{year}' ")
    elif year != 'NULL' and club_name != 'NULL':
        booths = database.query(
            f"SELECT booths.id, YEAR(booths.time_created), booths.club_id, booths.club_description, clubs.name FROM booths JOIN clubs ON booths.club_id = clubs.club_id WHERE booths.status = 1 and YEAR(booths.time_created) = '{year}' and clubs.name = '{club_name}' ")
    elif club_name == 'NULL' and year == 'NULL':
        booths = database.query(
            f"SELECT booths.id, YEAR(booths.time_created), booths.club_id, booths.club_description, clubs.name FROM booths JOIN clubs ON booths.club_id = clubs.club_id WHERE booths.status = 1")

    context = {}
    context["data"] = []
    list = ['id', 'time_created', 'club_id', 'club_description', 'club_name']

    for tup in booths:
        club_name_tup = database.query(f"SELECT name FROM clubs WHERE id = {tup[2]}")
        club_name = club_name_tup[0]
        context["data"].append(
            {list[0]: tup[0], list[1]: tup[1], list[2]: tup[2], list[3]: tup[3], list[4]: club_name})
    print(context)
    context = json.dumps(context)
    return HttpResponse(context)


class ArchiveCffBooths(DBRead):
    template_name = "app_club_ff/archive_cff_booths_page.html"

    def get_context_data(self, request,  *args, **kwargs):
        context = {}
        booths = self.database.query(
            "SELECT id, time_created, club_id, club_description FROM booths WHERE `status` = 1")

        context["data"] = []
        list = ['id', 'time_created', 'club_id', 'club_description', 'club_name']

        for tup in booths:
            c_name = self.database.query(f"SELECT name FROM clubs WHERE id = {tup[2]}")
            c_name = c_name[0]
            context["data"].append(
                {list[0]: tup[0], list[1]: tup[1], list[2]: tup[2], list[3]: tup[3], list[4]: c_name[0]})
        return context
