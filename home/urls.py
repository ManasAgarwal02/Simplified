from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('signup/', views.handleSignup, name="signup"),
    path('login/', views.handleLogin, name="handleLogin"),
    path('logout/', views.handleLogout, name="logout")
]