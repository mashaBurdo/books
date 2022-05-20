from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_books/', views.all_books, name='all_books')
]