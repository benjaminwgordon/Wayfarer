<<<<<<< HEAD
from django.urls import path
=======
from django.urls import path, include
>>>>>>> 148c43c5ea1a22f87084893695bf1fab4674ffd0
from . import views


urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< HEAD
    
=======
    path('accounts/signup/', views.signup, name='signup')
>>>>>>> 148c43c5ea1a22f87084893695bf1fab4674ffd0
]