from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from . import models
from . import forms


def index(request):
    return HttpResponse("Hello, world.")


def all_books(request):
    books = models.Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'all_books.html', {'context': context})


def all_reviews(request):
    reviews = models.Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'all_reviews.html', {'context': context})


def book_detail(request, book_id):
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            book = get_object_or_404(models.Book, id=book_id)
            models.Review.objects.create(text=text, book=book)
            return redirect(reverse('book', args=[book_id]))
    else:
        form = forms.ReviewForm()
        book = get_object_or_404(models.Book, id=book_id)
        reviews = models.Review.objects.filter(book=book_id)
        context = {
            'form': form,
            'book': book,
            'reviews': reviews,
        }
        return render(request, 'book.html', {'context': context})
