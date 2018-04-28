"""Defines URL patterns for tangoDo"""

from django.conf.urls import url
import TangoDo.views as views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'^add_topic/$', views.add_topic, name='add_topic'),
    url(r'^add_entry/(?P<topic_id>\d+)/$', views.add_entry, name='add_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry')

]
