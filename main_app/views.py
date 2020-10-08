from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, City, Post

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
            return redirect ('post_index')
    posts = Post.objects.all()
    post_form = Post_Form()
    context = {'posts':posts, 'post_form':post_form}
        return render(request, 'posts/index.html', context)

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



