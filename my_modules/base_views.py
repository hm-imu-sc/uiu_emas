
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uiu_emas.settings')
import django
django.setup()

from django.shortcuts import redirect, render
from my_modules.database import MySql
from django.views.generic import View, TemplateView

import hashlib

# class classonlymethod(classmethod):
#     def __get__(self, instance, cls=None):
#         if instance is not None:
#             raise AttributeError("This method is available only on the class, not on instances.")
#         return super().__get__(instance, cls)


class DBRead(TemplateView):

    database = MySql.db()
    login_required = False
    logout_required = False

    def respond(self, request, *args, **kwargs):

        response = None
        verified = True
        user = None

        if self.login_required or self.logout_required:
            try:
                user = request.session["user"]
                if not self.__verify_user(user):
                    verified = False
            except KeyError:
                verified = False

        if verified:
            if self.logout_required:
                response = redirect(f"app_general:{user['domain']}_dashboard_page")
            else:
                response = self.__get_requested_response(request, *args, **kwargs)
        else:
            if self.logout_required:
                response = self.__get_requested_response(request, *args, **kwargs)
            else:
                response = redirect("app_general:login_page")

        return response

    def __get_requested_response(self, request, *args, **kwargs):
        kwargs["request"] = request
        context = self.get_context_data(*args, **kwargs)
        return render(request, self.template_name, context=context)

    def __verify_user(self, user):

        try:
            return user["login_status"]
        except TypeError or KeyError:
            return False
            
        # user_data = self.database.get(f"{user['domain']['name']}s", ["password_hash"], {
        #     user["domain"]["field"]: user["id"]
        # })[0]
        # identification_hash = hashlib.sha256(f"{user['id']}({user_data['password_hash']})".encode("ASCII")).hexdigest()
        
        # return user["identification_hash"] == identification_hash

    @classmethod
    def as_view(cls, login_required=False, logout_required=False):
        cls.login_required = login_required
        cls.logout_required = logout_required
        return cls().respond


class DBAction(View):

    database = MySql.db()
    login_required = False
    logout_required = False

    def __init__(self):
        self.redirect_url = None
        self.redirect_args = {}

    def action(self, request, **kwargs):
        pass

    def respond(self, request, *args, **kwargs):

        response = None
        verified = True
        user = None

        if self.login_required or self.logout_required:
            try:
                user = request.session["user"]
                if not self.__verify_user(user):
                    verified = False
            except KeyError:
                verified = False

        if verified:
            if self.logout_required:
                response = redirect(f"app_general:{user['domain']}_dashboard_page")
            else:
                response = self.__get_requested_response(request, *args, **kwargs)
        else:
            if self.logout_required:
                response = self.__get_requested_response(request, *args, **kwargs)
            else:
                response = redirect("app_general:login_page")

        return response

    def __get_requested_response(self, request, *args, **kwargs):
        self.action(request, **kwargs)
        return redirect(self.redirect_url, **self.redirect_args)

    def __verify_user(self, user):

        try:
            return user["login_status"]
        except TypeError or KeyError:
            return False

    @classmethod
    def as_view(cls, login_required=False, logout_required=False):
        cls.login_required = login_required
        cls.logout_required = logout_required
        return cls().respond
