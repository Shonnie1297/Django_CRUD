from dataclasses import fields
from django.shortcuts import generic 

from .models import Post

class PostCreateView(generic.CreateView):
    model = Post
    fields =  " __all__"
    success_url  = reverse_lazy( "blog:all")

class PostDetail(generic.DetailView):
    model = Post   

class PostUpdateView(generic.UpdateView):
    model = Post
    fields =  " __all__"
    success_url  = reverse_lazy( "blog:all") 

class PostDeleteView(generic.DeletelView):
    model = Post
    fields =  " __all__"
    success_url  = reverse_lazy( "blog:all")     