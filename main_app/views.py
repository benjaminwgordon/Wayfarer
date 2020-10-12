from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .models import Profile, City, Post
from .forms import Post_Form, Profile_Form, NewUserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ValidationError


# Create your views here

# City show view
@login_required
def city_detail(request, city_id):
    if request.method == 'POST':
        post_form = Post_Form(request.POST)
        if post_form.is_valid():
            post_form.save(commit=False)
            city = City.objects.get(id=city_id).id
            author = Profile.objects.get(id=request.user.profile.id).id
            post = Post(author_id=author, city_id=city, title=request.POST['title'], body=request.POST['body'])
            post.save()
            return redirect('post_detail', city_id=city_id, post_id=post.id)
        else:
            context = {
                'post_create_form_errors': post_form.errors,
                'currentCity': City.objects.get(id=city_id),
                'posts': Post.objects.filter(city=city_id),
                'cities': City.objects.all(),
                'post_form': Post_Form()
            }
            return render(request, 'cities/detail.html', context) 
    else:
        #handling the post_post route
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
    context = {
        'new_user_form': NewUserForm()
    }
    return render(request, 'home.html', context)

# Show Post View 
@login_required
def post_detail(request, city_id, post_id):
    city = City.objects.get(id=city_id)
    post = Post.objects.get(id=post_id)
    is_owner = Post.objects.get(id=post_id).author.id == request.user.profile.id
    post_form = Post_Form()
    context = {
        'city': city,
        'post': post,
        'post_form': post_form,
        'is_owner': is_owner
    }
    return render(request, 'posts/detail.html', context) 



# Post Delete
@login_required
def post_delete(request, city_id, post_id):
        error_message = ''
        if Post.objects.get(id=post_id).author.id == request.user.profile.id:
            post = Post.objects.get(id=post_id).delete()
            return redirect('city_detail', city_id=city_id)
        else:
            return redirect('post_detail', city_id=city_id, post_id=post_id)

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
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            context = {
                'form_errors': form.errors
            }
            return render(request, 'home.html', context)
    form = NewUserForm()
    context = {
        'form': form,
    }
    return render(request, 'home.html', context)

@login_required
def profile_details(request):
    # handle profile show
    posts = Post.objects.filter(author=request.user.profile.id)
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