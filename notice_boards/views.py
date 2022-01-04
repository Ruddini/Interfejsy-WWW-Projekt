from django.shortcuts import render,redirect
from .models import Topic, Notice
from .forms import TopicForm, NoticeForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404

def index(request):
    """Main site for notice_board app"""
    return render(request,'notice_boards/index.html')

def topics(request):
    """Show all Topics"""
    topics = Topic.objects.order_by('date_added')
    content = {"topics": topics}
    return render(request,'notice_boards/Topics.html',content)

def topic(request, topic_id):
    """Show one topic"""
    topic = Topic.objects.get(id=topic_id)
    notices = topic.notice_set.order_by('-date_added')
    content = {"topic": topic, "notices": notices}
    return render(request,'notice_boards/topic.html',content)

@login_required
def new_topic(request):
    """Add new topic"""
    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(data = request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            #new_topic.owner = request.user
            new_topic.save()
            return redirect('notice_boards:topics')

    content = {'form' : form}
    return render(request, 'notice_boards/new_topic.html',content)

@login_required
def new_notice(request, topic_id):
    """Add new Notice"""
    topic = Topic.objects.get(id=topic_id)

    if request.method!= "POST":
        form = NoticeForm()
    else:
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            new_notice = form.save(commit=False)
            new_notice.topic = topic
            new_notice.owner = request.user
            new_notice.save()
            return redirect('notice_boards:topic', topic_id=topic.id)
    content = {"form":form,"topic":topic}
    return render(request,'notice_boards/new_notice.html',content)

@login_required
def edit_notice(request, notice_id):
    """Edit existing notice"""
    notice = Notice.objects.get(id=notice_id)
    topic = notice.topic
    if notice.owner != request.user:
        raise Http404

    if request.method != "POST":
        form = NoticeForm(instance = notice)
    else:
        form = NoticeForm(request.POST, request.FILES,instance = notice)
        if form.is_valid():
            new_notice = form.save(commit=False)
            new_notice.topic = topic
            new_notice.save()
            return redirect('notice_boards:topic', topic_id=topic.id)
    content = {"form":form,"notice":notice}
    return render(request,'notice_boards/edit_notice.html',content)

def search(request):

    if request.method != "POST":
        pass
    else:
        searched = request.POST['searched']
        search_result = Topic.objects.filter(text__icontains=searched)

    content = {'searched': searched, 'search_result':search_result}
    return render(request,'notice_boards/search.html',content)

def contact(request):
    """Show contact site"""
    return render(request,'notice_boards/contact.html')