from django.conf import settings
from django.urls import path, include
from . import views
from app_cse_ps import urls as app_cse_ps_urls
from app_club_ff import urls as app_club_ff_urls

app_name = "app_admin"

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
]