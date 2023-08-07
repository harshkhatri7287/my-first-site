from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'title': 'first post',
        'author': 'Harsh Khatri',
        'createdOn': '28-01-2002',
        'content': 'Hello, this is my first post'
    },
    {
        'title': 'second post',
        'author': 'Manish Khatri',
        'createdOn': '05-09-2005',
        'content': 'Hello, this is my........ first post'
    }
]


def home(request):
    data = {'posts': posts}
    return render(request, 'blogs/home.html', data)


def about(request):
    return render(request, 'blogs/about.html', {'title': 'about'})


