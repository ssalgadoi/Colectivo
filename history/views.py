from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils.translation import get_language






def historia(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "history/historia.html", {'post': post})




def category(request, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    posts = category.get_history_posts.all()

    if category_id == 20:  # ID específico para la categoría especial
        template_name = 'history/valle.html'
    else:
        template_name = 'history/category.html'

    return render(request, template_name, {
        'category': category,
        'categories': categories,
        'posts': posts,
        'current_category': category.name,
    })

def audiovisual(request):
    # Obtener el idioma actual
    current_language = get_language()

    # Obtener las categorías 'Más' y 'More' en función del idioma
    category_names = {'es': 'Más', 'en': 'More'}
    category_name = category_names.get(current_language, 'Más')  # Por defecto 'Más'

    try:
        category = Category.objects.language(current_language).get(translations__name=category_name)
    except Category.DoesNotExist:
        category = None

    # Filtrar los posts que pertenecen a la categoría
    if category:
        posts = Post.objects.filter(category=category)
    else:
        posts = []

    categories = Category.objects.all()

    return render(request, "history/videos.html", {
        'posts': posts,
        'categories': categories,
        'current_category': category_name  # Pasar el nombre de la categoría actual al contexto
    })
