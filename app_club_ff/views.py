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

        student = self.database.query(f"SELECT student_id, name, uiu_email FROM students WHERE student_id = '{student_id}'")
        context["data"] = []
        list = ['student_id', 'name', 'uiu_email']
        for tup in student:
            context["data"].append({list[0]:tup[0],list[1]:tup[1], list[2]: tup[2]})
        return context
