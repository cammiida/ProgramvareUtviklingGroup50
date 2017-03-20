from django.contrib.auth.models import User
from django import forms
from .models import *

class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    # Info om klassen
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['name']

class Questions(forms.Form):
    question=forms.CharField(max_length=500)
    value=forms.IntegerField()
