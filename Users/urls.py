"""Defines URL patterns for tangoDo"""

from django.conf.urls import url
from django.contrib.auth.views import login
import Users.views as views

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
]
