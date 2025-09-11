from django.shortcuts import render , HttpResponse
from .models import Book
from django.contrib.auth.decorators import permission_required

# Create your views here.
def index(request):
    return HttpResponse("Welcome to my book shelf.")

@permission_required("bookshelf.view_book", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})