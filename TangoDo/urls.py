"""Defines URL patterns for tangoDo"""

from django.conf.urls import url
import TangoDo.views as views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic')
]
