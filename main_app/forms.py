from django.forms import ModelForm
from django import forms
from .models import City, Profile, Post


class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['city', 'author']

class Profile_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'current_city']
