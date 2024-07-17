from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils.translation import get_language






def historia(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "history/historia.html", {'post': post})




def category(request, category_id):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    posts = category.get_history_posts.all()  # Asegúrate de tener este método definido en tu modelo Category
    return render(request, "history/category.html", {
        'category': category,
        'categories': categories,
        'posts': posts,
        'current_category': category.name  # Pasar el nombre de la categoría actual al contexto
    })

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
    current_category_name = mas_category.name if mas_category else more_category.name if more_category else None

    return render(request, "history/videos.html", {
        'posts': posts,
        'categories': categories,
        'current_category': current_category_name  # Pasar el nombre de la categoría actual al contexto
    })




# def video_detail(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     return render(request, "history/video.html", {'post': post})