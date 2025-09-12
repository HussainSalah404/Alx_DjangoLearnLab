from django.shortcuts import render , HttpResponse
from .models import Book
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm

# Create your views here.
def index(request):
    return HttpResponse("Welcome to my book shelf.")

@permission_required("bookshelf.view_book", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

def example_form_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # Do something with the data (e.g., save or authenticate)
            return render(request, "form_example.html", {"form": ExampleForm(), "success": True})
    else:
        form = ExampleForm()

    return render(request, "form_example.html", {"form": form})