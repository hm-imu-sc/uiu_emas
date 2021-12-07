
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uiu_emas.settings')
import django
django.setup()

from django.shortcuts import redirect
from my_modules.database import MySql
from django.views.generic import View, TemplateView

class DBRead(TemplateView):

    database = MySql.db()

class DBAction(View):
    
    database = MySql.db()

    def __init__(self):
        self.redirect_url = None

    def action(self, request, **kwargs):
        pass
    
    def post(self, request, **kwargs):
        self.action(request, **kwargs)
        return redirect(self.redirect_url)

    def get(self, request, **kwargs):
        self.action(request, **kwargs)
        return redirect(self.redirect_url)
