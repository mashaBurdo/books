from django.http import HttpResponse
from django.shortcuts import render
from . import models


def index(request):
    return HttpResponse("Hello, world.")


def all_books(request):
    books = models.Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'all_books.html', {'context': context})