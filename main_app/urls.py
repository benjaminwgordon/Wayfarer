
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profiles/<int:profile_id>/', views.profile_details, name='profile_detail')
]