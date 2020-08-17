from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post  # as we are in the same path as of the model .model works


# posts = [
#     {
#         'author': 'Soumya',
#         'title': 'Blog1',
#         'date_posted': '28th June 2021',
#         'content': 'Action'
#     },
#     {
#         'author': 'R K Jena',
#         'title': 'Blog2',
#         'date_posted': '28th June 2021',
#         'content': 'News'
#     }
# ]
# The above posts was created for static analysis in the earlier lessons

# Create your views here.

# The below 2 lines were being created for first time how the Django works
# def home(request):
#     return HttpResponse('<h1>Blog homepage </h1>')

# Below are the lines which we will use to render html files
def home(request):  # This is our home function
    context = {
        # 'posts': posts # This was used earlier when we created dummy data
        'posts': Post.objects.all()  # This we are using to get the all objects we have stored in Post model
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):  # This is our Home class view
    model = Post
    template_name = "blog/home.html"  # we have already created a home html, we have just assigned it
    # as the template name for this class. <app>/<model>_<viewtype>.html (This is the default one which
    # Django was looking for but we replaced it with our existing home.html)
    context_object_name = 'posts'  # This tells the browser which object to load into the class
    ordering = ['-date_posted']  # - symbol tells that to arrange the posts from newest to oldest
    # according to the date_posted
    paginate_by = 2  # This will work for pagination


class UserPostListView(ListView):  # This is our Home class view
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    # Now let's create the URL pattern which django expects  <app>/<model>_<viewtype>.html rather than
    # pointing to out self created html file


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']  # This is the fields we want to see in the template

    def form_valid(self, form):
        form.instance.author = self.request.user  # We are setting the author before the form valid method runs
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']  # This is the fields we want to see in the template

    def form_valid(self, form):
        form.instance.author = self.request.user  # We are setting the author before the form valid method runs
        return super(PostUpdateView, self).form_valid(form)

    def test_func(self):  # this will prevent any user update other's post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):  # this will prevent any user update other's post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# The below 2 lines were being created for first time how the Django works
# def about(request):
#     return HttpResponse('<h1>Blog About page </h1>')

# Below are the lines which we will use to render html files
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
