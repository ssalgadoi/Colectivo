from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils.translation import get_language





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



# Page Video

def audiovisual(request):
    # Obtener el idioma actual
    current_language = get_language()

    # Obtener las categorías 'Más' y 'More'
    try:
        mas_category = Category.objects.language('es').get(translations__name='Más')
    except Category.DoesNotExist:
        mas_category = None
    
    try:
        more_category = Category.objects.language('en').get(translations__name='More')
    except Category.DoesNotExist:
        more_category = None
    
    # Filtrar los posts que pertenecen a las categorías 'Más' y 'More'
    categories_to_filter = []
    if mas_category:
        categories_to_filter.append(mas_category)
    if more_category:
        categories_to_filter.append(more_category)

    if categories_to_filter:
        posts = Post.objects.filter(category__in=categories_to_filter)
    else:
        posts = []

    categories = Category.objects.all()
    return render(request, "history/videos.html", {'posts': posts, 'categories': categories})

def video_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    # Verifica si la categoría del post es 'El Valle de los Negros'
    if post.category.id == 9:
        template_name = "history/valle.html"
    else:
        template_name = "history/video.html"
    
    return render(request, template_name, {'post': post})
