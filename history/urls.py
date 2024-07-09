from django.urls import path
from . import views

urlpatterns = [
    path('', views.history, name='historias'),
    path('historia/<int:post_id>/', views.historia, name='historia'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('videos/', views.audiovisual, name='videos'),
    path('video/<int:post_id>/', views.video_detail, name='video_detail'),
]
