from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
posts = [
    {
        'title': 'Blog Post - 1',
        'author': 'Ali Hassan',
        'date_posted': 'August 19, 2020',
        'content': 'This is first blog post which is about cloud tech'
    },
    {
        'title': 'Blog Post - 2',
        'author': 'Ahmad Raza',
        'date_posted': 'July 20, 2020',
        'content': 'This is second blog post which is about law firms'
    }
]


def home(request):
    context = {
            'data': Post.objects.all()
        }
    return render(request, 'blog/home.html', context=context)
    # return HttpResponse('<h1>Blog Home-123</h1>' )


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def welcome(request):
    return HttpResponse('Welcome page')
