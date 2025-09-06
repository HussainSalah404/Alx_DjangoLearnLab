from django.shortcuts import render, HttpResponse
from relationship_app.models import Book

# Create your views here.
def index(request):
    return HttpResponse("Welcome to my book shelf.")

def book_list(request):
    """Retrieves all books and renders a template displaying the list."""
    books = Book.objects.all()  # Fetch all book instances from the database
    context = {'book_list': books}  # Create a context dictionary with book list
    return render(request, 'relationship_app/list_books.html', context)

