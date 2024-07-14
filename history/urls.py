from django.urls import path
from . import views

urlpatterns = [
    # Esta ruta ahora apunta a 'historias'
    path('historia/<int:post_id>/', views.historia, name='historia'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('videos/', views.audiovisual, name='videos'),
]