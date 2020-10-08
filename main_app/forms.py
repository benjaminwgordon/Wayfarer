from django.forms import ModelForm
from .models import City, Profile, Post


class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'city', 'title', 'body', 'created_at']
