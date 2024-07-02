from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'blog-home'), # be specific about the route path names
    path('about/', views.about, name='blog-about'),
]
