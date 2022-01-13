
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uiu_emas.settings')
import django
django.setup()

from django.shortcuts import redirect, render
from my_modules.database import MySql
from django.views.generic import View, TemplateView


class classonlymethod(classmethod):
    def __get__(self, instance, cls=None):
        if instance is not None:
            raise AttributeError("This method is available only on the class, not on instances.")
        return super().__get__(instance, cls)


class DBRead(TemplateView):

    database = MySql.db()
    login_required = False

    def respond(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)
        response = render(request, self.template_name, context=context)

        if self.login_required:

            user = None
            
            try:
                user = request.COOKIES["user"]
            except KeyError:
                response = redirect("app_general:login_page")

        # cookie_expires = datetime.now() - timedelta(hours=60)
        # cookie_expires = cookie_expires.strftime("%a, %d-%b-%Y %H:%M:%S GMT+6")
        # response.set_cookie("key", "value", expires=cookie_expires)
        # print(request.COOKIES)

        return response

    @classonlymethod
    def as_view(cls, login_required=False):
        cls.login_required = login_required
        return cls().respond


class DBAction(View):

    database = MySql.db()

    def __init__(self):
        self.redirect_url = None

    def action(self, request, **kwargs):
        pass

    def respond(request, *args, **kwargs):
        pass

    def post(self, request, **kwargs):
        self.action(request, **kwargs)
        return redirect(self.redirect_url)

    def get(self, request, **kwargs):
        self.action(request, **kwargs)
        return redirect(self.redirect_url)
