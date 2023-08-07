from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='blog-panel'),
    path('home/', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]