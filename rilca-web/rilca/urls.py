from django.conf.urls import url, include
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.contrib.auth import views as auth_views
from django.contrib import admin

from pa import views

urlpatterns = [
    url(r'^organization$', views.Organization.as_view(), name="organization"),
    url(r'^items$', views.ItemList.as_view(), name="pa-items-list"),
    url(r'^new/document$', views.NewDocument.as_view(), name="new-document"),
    url(r'^document/(?P<year>[0-9]{2})/(?P<staff_id>.*)$', views.FillDocument.as_view(), name="fill-document"),
    url(r'^documents$', views.DocumentList.as_view(), name="pa-documents-list"),
    url(r'^form$', views.Form.as_view(), name="form"),
    url(r'^admin/', admin.site.urls),
    url(r'^login', auth_views.login, {'template_name': 'login.html'}, name="login"),
    url(r'^logout', auth_views.logout, {'template_name': 'logout.html'}, name="logout"),
]
