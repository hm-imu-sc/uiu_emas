from django.shortcuts import render
from my_modules.base_views import DBAction
from django.views.generic import TemplateView

# Create your views here.

class Index(TemplateView):
    template_name = "app_cse_ps/index.html"

    def get_context_data(self, *args, **kwargs):
        return super().get_context_data(*args, **kwargs)
