from django.shortcuts import render
from .models import Post

def articles(request):
    posts = Post.objects.all()
    return render(request, "articles/articulos.html", {'posts': posts})
