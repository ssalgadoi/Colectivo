from django.shortcuts import render, get_object_or_404
from .models import Post 
from history.models import Category



def valle(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, "valle/valle.html", {'posts': posts, 'categories': categories})
