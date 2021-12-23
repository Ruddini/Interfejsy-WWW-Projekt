"""Define URL-s for notice_boards app"""
from django.urls import path

from . import views

app_name = "notice_boards"
urlpatterns = [
    #main site
    path('',views.index,name='index'),
    #all topics
    path('topics/',views.topics,name='topics'),
    #one topic, all notices of this topic
    path('topics/<int:topic_id>/',views.topic, name='topic'),
    #add new topic
    path('new_topic/',views.new_topic, name='new_topic'),
    #add new notice
    path('new_notice/<int:topic_id>/',views.new_notice, name='new_notice'),
    #edit notice
    path('edit_notice/<int:notice_id>/',views.edit_notice, name="edit_notice"),
    #Search
    path('search/',views.search, name='search')

]