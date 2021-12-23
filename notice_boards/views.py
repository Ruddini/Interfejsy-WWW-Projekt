from django.shortcuts import render,redirect
from .models import Topic, Notice
from .forms import TopicForm, NoticeForm

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

def new_topic(request):
    """Add new topic"""
    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('notice_boards:topics')

    content = {'form' : form}
    return render(request, 'notice_boards/new_topic.html',content)

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
            new_notice.save()
            return redirect('notice_boards:topic', topic_id=topic.id)
    content = {"form":form,"topic":topic}
    return render(request,'notice_boards/new_notice.html',content)

def edit_notice(request, notice_id):
    """Edit existing notice"""
    notice = Notice.objects.get(id=notice_id)
    topic = notice.topic

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