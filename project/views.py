from django.shortcuts import render
from .models import Post

def project(request):
    posts = Post.objects.all()
  
    return render(request, "project/proyectos.html", {'posts': posts})
