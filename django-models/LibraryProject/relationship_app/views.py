from django.views.generic.detail import DetailView
from django.shortcuts import render, HttpResponse
from .models import Library, Book

# Create your views here.

def index(request):
    # A simple welcome page for your app
    return HttpResponse("Welcome to my book shelf.")

def list_books(request):
    """Retrieves all books and renders a template displaying the list."""
    books = Book.objects.all()  # Fetch all book instances from the database
    context = {'list_books': books}  # Context dictionary with book list
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    """Displays details of a specific library and its related books."""
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"  # In template, use {{ library }}

    def get_context_data(self, **kwargs):
        # Start with the default context (which already has {{ library }})
        context = super().get_context_data(**kwargs)
        # Add all related books to the same variable name used in list_books
        context["list_books"] = self.object.books.all()
        return context