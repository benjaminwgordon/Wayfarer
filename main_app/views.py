from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, City, Post
from .forms import Post_Form, Profile_Form
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here



# City show view
@login_required
def city_detail(request, city_id):
    cities = City.objects.all()
    city = City.objects.get(id=city_id)
    posts = Post.objects.filter(city=city_id)
    context={
        'currentCity':city,
        'cities': cities,
        'posts': posts,
        'post_form': Post_Form()
        }
    return render(request, 'cities/detail.html', context)

#  Home view
def home(request):
    return render(request, 'home.html')

# Index & Create View 
@login_required
def post_create(request, city_id):
    if request.method == 'POST':
        post_form = Post_Form(request.POST)
        if post_form.is_valid():
            post_form.save()
            post_form
            return redirect('city_detail', city_id=city_id)

# Show Post View 
@login_required
def post_detail(request, city_id, post_id):
    city = City.objects.get(id=city_id)
    post = Post.objects.get(id=post_id)
    post_form = Post_Form()
    context = {
        'city': city,
        'post': post,
        'post_form': post_form
    }
    return render(request, 'posts/detail.html', context) 



# Post Delete
@login_required
def post_delete(request, city_id, post_id):
    post = Post.objects.get(id=post_id).delete()
    return redirect('city_detail', city_id=city_id)

# Post Edit
@login_required
def post_edit(request, city_id, post_id):
    city = City.objects.get(id=city_id)
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        post_form = Post_Form(request.POST, instance = post)
        if post_form.is_valid(): 
            post_form.save()
            return redirect('post_detail', post_id = post_id, city_id = city_id)
    else:
        post_form = Post_Form(instance = post)
        context = {
            'post':post, 
            'post_form':post_form,
            'city': city
        }
        return render(request, 'posts/edit.html', context)

# Create your views here.

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        email = request.POST['email']
        confirm_email = request.POST['confirm_email']
        if form.is_valid() and email == confirm_email:
            user = form.save(commit=False)
            user.email = email
            user.save()
            login(request, user)
            return redirect('profile_edit')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request, 'home.html', context)

@login_required
def profile_details(request):
    # handle profile show
    posts = Post.objects.filter(author=request.user.profile)
    profile_form = Profile_Form()
    print("posts: ", posts)
    context = {
        'profile': request.user.profile,
        'posts': posts,
        'profile_form':profile_form,
    }
    return render(request, 'registration/profile.html', context)

@login_required
def profile_edit(request):
    if request.method == "POST":
        #handle profile update
        profile_form = Profile_Form(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile')
    else:
        #handle profile edit
        profile_form = Profile_Form(instance=request.user.profile)
        context = {
            'profile': request.user.profile,
            'profile_form': profile_form
        }
        return render(request, 'registration/profile_edit.html', context)

@login_required
def profile_delete(request):
    user = request.user
    logout(request)
    user.delete()
    return redirect('home')