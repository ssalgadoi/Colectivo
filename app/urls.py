from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.i18n import set_language


urlpatterns = [
    #Path admin
    path('admin/', admin.site.urls),
    #Path base
    path('', include('base.urls')),
    # Path de pages
    path('page/', include('pages.urls')),
    # # Path de history
    path('historias/', include('history.urls')),
    # Path de image
    path('fotografias/', include('image.urls')),
    # Path de project
    path('proyectos/', include('project.urls')),
   # Path de articles
    path('articulos/', include('articles.urls')),
   
  
  
    # Path de Idioma
    path('set-language/', set_language, name='set_language'),  
    
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)