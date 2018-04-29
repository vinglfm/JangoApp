from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from TangoDo.models import Topic, Entry
from TangoDo.forms import TopicForm, EntryForm


# Create your views here.


def index(request):
    """Home page for Tango Do"""
    return render(request, 'TangoDo/index.html')


@login_required
def topics(request):
    """Show all topics"""
    topics = Topic.objects.filter(user=request.user).order_by('add_date')
    return render(request, 'TangoDo/topics.html', {'topics': topics})


@login_required
def topic(request, topic_id):
    """Show selected topic"""
    topic = Topic.objects.get(id=topic_id)

    if topic.user != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-add_date')
    return render(request, 'TangoDo/topic.html', {'topic': topic, 'entries': entries})


@login_required
def add_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = request.user
            topic.save()
            return HttpResponseRedirect(reverse('tango_do:topics'))
    return render(request, 'TangoDo/add_topic.html', {'form': form})


@login_required
def add_entry(request, topic_id):
    """Add a new entry to topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.topic = topic
            entry.save()
            return HttpResponseRedirect(reverse('tango_do:topic', args=[topic_id]))
    return render(request, 'TangoDo/add_entry.html', {'topic': topic, 'form': form})


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.user != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tango_do:topic', args=[topic.id]))
    return render(request, 'TangoDo/edit_entry.html', {'entry': entry, 'topic': topic, 'form': form})
