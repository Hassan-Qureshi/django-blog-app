from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
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


# Using `LoginRequiredMixin` because we want to validate if the user is logged in or not.
class PostCreateView(LoginRequiredMixin, CreateView):
    # We need to create the post so there will be a form for this we only need fields which should be in the form
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        """
        Overriding form method because there should be a user who create the post and
        that user should be logged in user.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # In order to stop other users to edit your post we have to extend class-based view to UserPassesTestMixin
    # and override the following method

    def test_func(self):
        # Get the post being updated
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    # success_url is required because once post is deleted it will automatically redirected towards home page
    success_url = '/'

    def test_func(self):
        # Get the post being updated
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def welcome(request):
    if request:
        return HttpResponse('Welcome page')
