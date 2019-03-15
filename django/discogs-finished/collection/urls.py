from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('releases/<int:id>', views.release, name='release'),
]
