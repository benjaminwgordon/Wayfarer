from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< HEAD
    
=======
    path('accounts/signup/', views.signup, name='signup')
<<<<<<< HEAD
]

=======
>>>>>>> 148c43c5ea1a22f87084893695bf1fab4674ffd0
]
>>>>>>> 9a86ff242276efea7fa75f039abd53daab6fa7d0
