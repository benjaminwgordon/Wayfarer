from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, City, Post
from .forms import Post_Form

# Create your views here


#  Home view

def home(request):
    return render(request, 'home.html')

# Index & Create View 

def post_index(request):
    if request.method == 'POST':
        post_form = Post_Form(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('post_index')
    posts = Post.objects.all()
    post_form = Post_Form()
    context = {'posts':posts, 'post_form': post_form}
    return render(request, 'posts/index.html', context)

# Show Post View 

def post_details(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/detail.html', {'post': post}) 

# Create your views here.

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cities_index')
        error_message +='\nInvalid sign up - try again'
    form = UserCreationForm()
    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request, 'registration/signup.html', context)



