from django.shortcuts import render, get_object_or_404
from .models import Post, Category





def history(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, "history/historias.html", {'posts': posts, 'categories': categories})

def historia(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "history/historia.html", {'post': post})


def category(request, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    posts = category.get_history_posts.all()  # Accede a los posts a través de la relación definida en el modelo Post
    return render(request, "history/category.html", {'category': category, 'categories': categories, 'posts': posts})


def audiovisual(request):
    # Obtener la categoría 'Más'
    try:
        mas_category = Category.objects.get(translations__name='Más')
    except Category.DoesNotExist:
        mas_category = None
    
    # Filtrar los posts que pertenecen a la categoría 'Más'
    if mas_category:
        posts = Post.objects.filter(category=mas_category)
    else:
        posts = []

    categories = Category.objects.all()
    return render(request, "history/videos.html", {'posts': posts, 'categories': categories})

def video_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "history/video.html", {'post': post})

