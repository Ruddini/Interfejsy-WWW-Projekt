from django import forms

from .models import Topic, Notice

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {"text":''}


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title','text','image']
        labels = {'title':'','text':'','image':''}
        widgets = {"text": forms.Textarea(attrs={"cols":80})}
