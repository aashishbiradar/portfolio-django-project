from django.shortcuts import render
from .models import Blog

def bloghome(req):
    blogs = Blog.objects
    return render(req,'blog/bloghome.html', {'blogs' : blogs})
