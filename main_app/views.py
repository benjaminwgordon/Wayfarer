from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, City, Post

# Create your views here


#  Home view

def home(request):
    return render(request, 'home.html')

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



