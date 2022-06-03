from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('books', views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("", views.index, name="index"),
    path("login_view/", views.login_view, name="login_view"),
    path("logout_view/", views.logout_view, name="logout_view"),
    path("all_books/", views.all_books, name="all_books"),
    path("all_reviews/", views.all_reviews, name="all_reviews"),
    path("book/<int:book_id>/", views.book_detail, name="book"),
]
