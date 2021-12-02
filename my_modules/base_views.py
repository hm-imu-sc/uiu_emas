
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'minecraft_crafting_assistant.settings')
import django
django.setup()

from django.shortcuts import redirect
from my_modules.database import MySql
from django.views.generic import View, CreateView

class DBAction(View):
    
    database = MySql()

    def __init__(self):
        self.redirect_url = None

    def action(self, request, **kwargs):
        pass
    
    def post(self, request, **kwargs):
        self.action(request, **kwargs)
        return redirect(self.redirect_url)

    def get(self, request, **kwargs):
        return redirect(self.redirect_url)
