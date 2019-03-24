from django.db import models
from django import forms
from .models import Team,UserTasks
from django.contrib.auth.models import User


class TaskCreationForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(TaskCreationForm,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['task_title'].widget.attrs.update({"class":"form-control","placeholder":"Enter Title for task"})
        self.fields['task_description'].widget = forms.Textarea(attrs={"class":"form-control ","placeholder":"Enter Description for the task"})
        self.fields['task_comments'].widget = forms.Textarea(attrs={"class":"form-control ","placeholder":"Comments for task","rows":"5"})
        self.fields['task_comments'].required = False
    class Meta:
        model = UserTasks
        fields =['task_title','task_description','task_comments']

class TeamCreationForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(TeamCreationForm,self).__init__(*args,**kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs.update({"class":"form-control","placeholder":"Enter Name for Team"})
        self.fields['description'].widget.attrs.update({"placeholder":"Enter A Short Description About Your Team"})
    class Meta:
        model = Team
        fields = ['name','description']

class AddUserToTeam(forms.Form):
    member_username = forms.CharField(label="Member Username",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username of the member you wish to add'}))

class TeamTaskCreationForm(TaskCreationForm):
    assignee = forms.CharField(label="Assignee",widget=forms.TextInput(attrs={"class":'form-control','placeholder':'Assign the task to ?'}))