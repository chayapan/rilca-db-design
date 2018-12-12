from django.conf.urls import url, include
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.contrib.auth import views as auth_views
from django.contrib import admin

from pa import views

urlpatterns = [
    url(r'^form$', views.Form.as_view(), name="customer"),
    url(r'^admin/', admin.site.urls),
    url(r'^login', auth_views.login, {'template_name': 'login.html'}, name="login"),
    url(r'^logout', auth_views.logout, {'template_name': 'logout.html'}, name="logout"),
]
