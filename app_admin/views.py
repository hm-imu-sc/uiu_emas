from django.shortcuts import render
from my_modules.base_views import DBAction,DBRead
from django.views.generic import TemplateView
from my_modules.database import MySql

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
    database = MySql.db()

    def get_context_data(self, *args ,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        trimesters = self.database.query(f'SELECT DISTINCT trimester FROM sections')
        context['trimesters'] = list(trimesters[0])
        print(context)
        return context

