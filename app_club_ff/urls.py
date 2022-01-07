from django.conf import settings
from django.urls import path
from . import views

from django.shortcuts import render
from my_modules.base_views import DBAction, DBRead
from django.views.generic import TemplateView
from my_modules.database import MySql
from django.http import HttpResponse
import json

app_name = "app_club_ff"

urlpatterns = [
    path("index/", views.Index.as_view(), name="index"),
    path("fest_registration_page/<student_id>",views.FestRegistrationPage.as_view(), name="fest_registration_page"),


]
