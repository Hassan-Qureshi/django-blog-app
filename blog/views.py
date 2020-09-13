from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)


def home(request):
    context = {
            'data': Post.objects.all()
        }
    return render(request, 'blog/home.html', context=context)


class PostListView(ListView):
    model = Post
    # If we don't set template_name by default it is looking for template
    # like this <app>/<model>_<view-type>.html i.e blog/post_list.html.
    template_name = 'blog/home.html'
    # We need to set the context_object_name because we are using 'data' in our template and looping over it
    # By default, ListView uses `object_list` as variable in template on which we are looping in blog/home.html
    context_object_name = 'data'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    # we will not be setting context_object_name


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def welcome(request):
    return HttpResponse('Welcome page')
