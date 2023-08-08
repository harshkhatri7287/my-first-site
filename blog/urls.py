from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='blog-panel'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('about/', views.about, name='blog-about'),
]
