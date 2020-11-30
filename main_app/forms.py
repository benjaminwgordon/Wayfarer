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

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title.strip()) < 1:
            raise forms.ValidationError("title is required")
        if len(title.strip()) > 100:
            raise forms.ValidationError("title cannot be longer than 100 characters")
        return title

    def clean_body(self):
        body = self.cleaned_data['body']
        if len(body.strip()) < 1:
            raise forms.ValidationError("body is required")
        return body

class Profile_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'current_city']


class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for field in ['username','email', 'password1', 'password2']:
            self.fields[field].help_text = None

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already in Use")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already in Use")
        return username