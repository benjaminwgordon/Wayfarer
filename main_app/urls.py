from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('post/', views.post_index, name='post_index'),

    # path('cats/', views.cats_index, name='cats_index'),


]

