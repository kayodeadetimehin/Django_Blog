from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from blog.models import Post

# Create your views here.

class PostTemplateView(TemplateView):
    template_name = 'blog/about.html'

class PolicyView(TemplateView):
    template_name = 'blog/policy.html'

class PostListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-date_created')
    model = Post
    template_name = 'blog/home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
