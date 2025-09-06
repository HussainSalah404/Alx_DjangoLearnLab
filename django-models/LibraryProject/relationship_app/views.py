from django.views.generic.detail import DetailView
from django.shortcuts import render, HttpResponse
from .models import Library, Book
# Create your views here.
def index(request):
    return HttpResponse("Welcome to my book shelf.")

def list_books(request):
    """Retrieves all books and renders a template displaying the list."""
    books = Book.objects.all()  # Fetch all book instances from the database
    context = {'list_books': books}  # Create a context dictionary with book list
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()
        return context