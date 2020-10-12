from django.forms import ModelForm
from django import forms
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

class Profile_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'current_city']


