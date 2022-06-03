from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from . import forms, models


def index(request):
    return HttpResponse("Hello, world.")


def all_books(request):
    books = models.Book.objects.all()
    context = {
        "books": books,
    }
    return render(request, "all_books.html", {"context": context})


def all_reviews(request):
    reviews = models.Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, "all_reviews.html", {"context": context})


def book_detail(request, book_id):
    if request.method == "POST":
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            book = get_object_or_404(models.Book, id=book_id)
            models.Review.objects.create(text=text, book=book)
            return redirect(reverse("book", args=[book_id]))
    elif request.method == "GET":
        form = forms.ReviewForm()
        book = get_object_or_404(models.Book, id=book_id)
        reviews = models.Review.objects.filter(book=book_id)
        context = {
            "form": form,
            "book": book,
            "reviews": reviews,
        }
        return render(request, "book.html", {"context": context})


def login_view(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # username = request.POST['username']
            # password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("all_books"))
            else:
                raise PermissionDenied
    elif request.method == "GET":
        form = forms.LoginForm()
        context = {
            "form": form,
        }
        return render(request, "login.html", {"context": context})


def logout_view(request):
    logout(request)
    return redirect(reverse("all_books"))
