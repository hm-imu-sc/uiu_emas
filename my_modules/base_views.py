
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uiu_emas.settings')
import django
django.setup()

from django.shortcuts import redirect, render
from my_modules.database import MySql

class ViewBase:

    database = MySql.db()
    login_required = False
    logout_required = False

    def respond(self, request, *args, **kwargs):

        response = None
        verified = True
        user = None

        if self.login_required or self.logout_required:
            verified = self.__verify_user(request)

            if verified:
                user = request.session["user"]
        else:
            request.session["user"] = {}

        if verified:
            if self.logout_required:
                response = redirect(f"app_general:{user['domain']}_dashboard_page")
            else:
                response = self._get_requested_response(request, *args, **kwargs)
        else:
            if self.logout_required:
                response = self._get_requested_response(request, *args, **kwargs)
            else:
                response = redirect("app_general:login_page")

        return response

    def _get_requested_response(self, request, *args, **kwargs):
        pass

    def __verify_user(self, request):
        try:
            return request.session["user"]["login_status"]
        except KeyError:
            request.session["user"] = {"login_status": False}
            return False

    @classmethod
    def as_view(cls, login_required=False, logout_required=False):
        cls.login_required = login_required
        cls.logout_required = logout_required
        return cls().respond


class DBRead(ViewBase):

    def _get_requested_response(self, request, *args, **kwargs):
        context = self.get_context_data(request, *args, **kwargs)
        context["session"] = {"user": request.session["user"]}
        return render(request, self.template_name, context=context)
    
    def get_context_data(self, request, *args, **kwargs):
        return {}


class DBAction(ViewBase):

    def _get_requested_response(self, request, *args, **kwargs):
        self.redirect_args = {}
        self.redirect_url = None

        self.action(request, **kwargs)

        return redirect(self.redirect_url, **self.redirect_args)

    def action(self, request, **kwargs):
        pass
