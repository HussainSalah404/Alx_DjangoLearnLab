from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.http import HttpResponse
from .models import Library, Book
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView

# --- General Views ---
def index(request):
    return render(request, "relationship_app/index.html")


def list_books(request):
    """Retrieves all books and renders a template displaying the list."""
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"list_books": books})


class LibraryDetailView(DetailView):
    """Displays details of a specific library and its related books."""
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_books"] = self.object.books.all()
        return context


class register(CreateView):
    """Handles user registration using Django's built-in UserCreationForm."""
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"


# --- Role Check Helpers ---
def is_admin(user):
    return user.is_authenticated and hasattr(user, "userprofile") and user.userprofile.role == "Admin"


def is_librarian(user):
    return user.is_authenticated and hasattr(user, "userprofile") and user.userprofile.role == "Librarian"


def is_member(user):
    return user.is_authenticated and hasattr(user, "userprofile") and user.userprofile.role == "Member"


# --- Role-Based views ---
@user_passes_test(is_admin, login_url="/no-permission/")
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(is_librarian, login_url="/no-permission/")
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(is_member, login_url="/no-permission/")
def member_view(request):
    return render(request, "relationship_app/member_view.html")


# --- No Permission Page ---
def no_permission(request):
    return HttpResponse("Sorry, you don’t have permission to access this page.")


# --- Redirect Users Based on Role ---
def role_based_redirect(request):
    if request.user.is_authenticated:
        role = request.user.userprofile.role
        if role == "Admin":
            return redirect("admin_view")
        elif role == "Librarian":
            return redirect("librarian_view")
        elif role == "Member":
            return redirect("member_view")
    return redirect("index")

# View to add a book
class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('book-list')
    permission_required = 'relationship_app.can_add_book'

# View to edit a book
class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'relationship_app/book_form.html'
    success_url = reverse_lazy('book-list')
    permission_required = 'relationship_app.can_change_book'

# View to delete a book
class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'relationship_app/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')
    permission_required = 'relationship_app.can_delete_book'