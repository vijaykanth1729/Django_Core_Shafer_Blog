from django.shortcuts import render, redirect
from .models import Post
from .forms import CreatePostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#class based views follows...
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #by default looks for (<app_name>/<model>_<viewtype.html>)
    # Looks for blog/post_list.html
    context_object_name = 'posts'  #looks for object_list(Default)
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    # default template looks for blog/post_detail.html
    # default context objects it looks for 'object'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title', 'content')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ('title', 'content')

    def form_valid(self, form):
        #it ties author to the post before submitting to server..
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        #allowws only valid users can update their posts..
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        #allowws only valid users can update their posts..
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
#Function based views follows....

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
def about(request):
    return render(request, 'blog/about.html')

@login_required
def create_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Creation of New post is Success")
            return redirect('home')
    else:
        form = CreatePostForm()
    return render(request, 'blog/create_post.html', {'form':form})
