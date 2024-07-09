from django.shortcuts import render, get_object_or_404
from .models import Post, PostImage
# from history.models import Category

# Create your views here.

def image(request):
    posts = Post.objects.all()
    return render(request, "image/fotografias.html", {'posts':posts})

def fotografia(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "image/fotografia.html", {'post': post})