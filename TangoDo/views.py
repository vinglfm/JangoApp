from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from TangoDo.models import Topic
from TangoDo.forms import TopicForm


# Create your views here.


def index(request):
    """Home page for Tango Do"""
    return render(request, 'TangoDo/index.html')


def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('add_date')
    return render(request, 'TangoDo/topics.html', {'topics': topics})


def topic(request, topic_id):
    """Show selected topic"""

    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-add_date')
    return render(request, 'TangoDo/topic.html', {'topic': topic, 'entries': entries})


def add_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tango_do:topics'))
    return render(request, 'TangoDo/add_topic.html', {'form': form})
