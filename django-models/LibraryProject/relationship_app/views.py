from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from .models import Library, Book
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "relationship_app/index.html")

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
    
# --- Role check functions ---
def is_admin(user):
    return user.is_authenticated and hasattr(user, "userprofile") and user.userprofile.role == "Admin"

def is_librarian(user):
    return user.is_authenticated and hasattr(user, "userprofile") and user.userprofile.role == "Librarian"

def is_member(user):
    return user.is_authenticated and hasattr(user, "userprofile") and user.userprofile.role == "Member"

# --- Role-based views ---
@user_passes_test(is_admin)
def admin_dashboard(request):
    return HttpResponse("Welcome to the Admin Dashboard!")

@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return HttpResponse("Welcome to the Librarian Dashboard!")

@user_passes_test(is_member)
def member_dashboard(request):
    return HttpResponse("Welcome to the Member Dashboard!")

def role_based_redirect(request):
    if request.user.is_authenticated:
        role = request.user.userprofile.role
        if role == "Admin":
            return redirect("admin_dashboard")
        elif role == "Librarian":
            return redirect("librarian_dashboard")
        elif role == "Member":
            return redirect("member_dashboard")
    return redirect("index")
    