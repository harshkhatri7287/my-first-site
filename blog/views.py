from django.shortcuts import render
from .models import Post, Employee
from django.utils import timezone


def post_list(request):
    Posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blogs/post_list.html', {'Posts': Posts})


def about(request):
    return render(request, 'blogs/about.html', {'title': 'about'})


def employee_list(request):
    Employees = Employee.objects.all()
    return render(request, 'blogs/employee_list.html', {'list_': Employees})
