from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")


def all_books(request):
    return HttpResponse('All books')