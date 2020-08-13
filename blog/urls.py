from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="blogIndex"),
    path('postComment/', views.postComment, name="postComment"),
    path('<str:smug>/', views.blogpost, name="blogPost")
]
