from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('post/', views.post_index, name='post_index'),
    path('post/<int:post_id>/', views.post_details, name='detail'),
    path('post/<int:post_id>/delete', views.post_delete, name='delete'),
    path('post/<int:post_id>/edit', views.post_edit, name='edit'),
]
