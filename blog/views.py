from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


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
