from django.forms import ModelForm
from .models import City, Profile, Post


class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'cities', 'title', 'body']
