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
    path("get_club_names/", views.get_club_names, name="get_club_names"),
    path("fest_registration/",views.FestRegistration.as_view(), name="fest_registration"),
    path("fest_feed_page/", views.FestFeed.as_view(),name="fest_feed_page"),
    path("post_processor/<club_id>/<criteria>/<offset>/", views.PostProcessor.as_view(), name="post_processor"),
]
