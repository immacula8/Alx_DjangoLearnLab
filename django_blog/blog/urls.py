from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Registration
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),

    # Profile
    path('profile/', views.profile, name='profile'),

    # Login & Logout (using Django's built-in auth views)
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('posts/', views.posts, name='posts'),
]
