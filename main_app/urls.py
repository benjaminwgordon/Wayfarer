from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', views.profile_details, name='profile'),
    path('accounts/delete', views.profile_delete, name='profile_delete'),
    path('accounts/edit', views.profile_edit, name='profile_edit'),
    path('city/<int:city_id>/post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('city/<int:city_id>/post/<int:post_id>/delete', views.post_delete, name='post_delete'),
    path('city/<int:city_id>/post/<int:post_id>/edit', views.post_edit, name='post_edit'),
    path('city/<int:city_id>/', views.city_detail, name="city_detail")
  
]