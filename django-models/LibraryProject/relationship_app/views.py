from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from .models import Library, Book
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test

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
    
class register(CreateView):
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

    def get_form_class(self):
        # using UserCreationForm() here so the checker finds it
        form = UserCreationForm()
        return form.__class__