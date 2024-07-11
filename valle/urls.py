from django.urls import path
from . import views

urlpatterns = [
    path('', views.valle, name='valle'),
    

]
