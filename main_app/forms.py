from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import City, Profile, Post
# 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# 

class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['city', 'author']


    def clean(self):
        body = self.cleaned_data['body']
        if len(body.strip()) < 1:
            raise forms.ValidationError("body is required")
        title = self.cleaned_data['title']
        if len(title.strip()) < 1:
            raise forms.ValidationError("title is required")
        if len(title.strip()) > 99:
            raise forms.ValidationError("title cannot be longer than 100 characters")
        return self.cleaned_data

class Profile_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'current_city']


class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already in Use")
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already in Use")
        return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
