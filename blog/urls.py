from django.urls import path
from . import views

urlpatterns = [
    path('', views.bloghome, name='bloghome'),
    path('<str:blog_urlkey>', views.blogpost, name='blogpost')
]