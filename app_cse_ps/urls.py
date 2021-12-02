from django.conf import settings
from django.urls import path
from . import views

app_name = "app_cse_ps"

urlpatterns = [
    path("index/", views.Index.as_view(), name="index"),
]