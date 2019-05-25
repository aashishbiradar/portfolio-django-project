from django.shortcuts import render, get_object_or_404
from .models import Blog

def bloghome(req):
    blogs = Blog.objects
    return render(req,'blog/bloghome.html', {'blogs' : blogs})

def blogpost(req,blog_urlkey):
    blog = get_object_or_404(Blog, urlkey=blog_urlkey)
    return render(req,'blog/blogpost.html',{'blog':blog})
