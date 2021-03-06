"""uiu_emas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_cse_ps import urls as app_cse_ps_urls
from app_club_ff import urls as app_club_ff_urls
from app_admin import urls as app_admin_urls
from app_general import urls as app_general_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include(app_admin_urls)),
    path('admin_django/', admin.site.urls),
    path('cse_ps/', include(app_cse_ps_urls), name="cse_ps"),
    path('club_ff/', include(app_club_ff_urls), name="club_ff"),
    path('general/', include(app_general_urls), name="general"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
