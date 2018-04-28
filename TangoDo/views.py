from django.shortcuts import render
from TangoDo.models import Topic


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

