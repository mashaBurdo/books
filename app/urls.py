from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_books/', views.all_books, name='all_books'),
    path('all_reviews/', views.all_reviews, name='all_reviews'),
    path('book/<int:book_id>/', views.book_detail, name='book'),
]