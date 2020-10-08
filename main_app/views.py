from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile, City, Post

# Create your views here


#  Home view

def home(request):
    return render(request, 'home.html')