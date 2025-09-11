from django.shortcuts import render , HttpResponse
from .models import Book
# Create your views here.
def index(request):
    return HttpResponse("Welcome to my book shelf.")

def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})