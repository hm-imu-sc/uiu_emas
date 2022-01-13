from django.conf import settings
from django.urls import path, include
from . import views
from app_cse_ps import urls as app_cse_ps_urls
from app_club_ff import urls as app_club_ff_urls

LOGIN_REQUIRED = True

app_name = "app_admin"

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("prize_giving_page/", views.PrizeGivingPage.as_view(), name="prize_giving_page"),
    path("give_award/", views.GiveAward.as_view(), name="give_award"),
    path("get_projects_by_course_code/<course_code>/", views.get_projects_by_course_code, name="get_projects_by_course_code"),
    path("get_courses_by_trimester/<trimester>/",views.get_course_by_trimester,name="get_course_by_trimester"),

]