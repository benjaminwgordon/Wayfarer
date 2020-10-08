from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', views.profile_details, name='profile'),
    path('accounts/delete', views.profile_delete, name='profile_delete'),
    path('accounts/edit', views.profile_edit, name='profile_edit'),
    path('post/', views.post_index, name='post_index'),
    path('post/<int:post_id>/', views.post_details, name='detail'),
    path('post/<int:post_id>/delete', views.post_delete, name='delete'),
    path('post/<int:post_id>/edit', views.post_edit, name='edit'),
]
