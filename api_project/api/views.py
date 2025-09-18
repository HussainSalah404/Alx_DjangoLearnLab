from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


# View for listing all books (read-only, requires authentication)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()               # The set of Book objects this view will return
    serializer_class = BookSerializer           # Serializer used to convert Book instances <-> JSON
    permission_classes = [IsAuthenticated]      # Only authenticated users can access this view


# ViewSet for full CRUD operations on books (requires authentication)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()               # The set of Book objects this view will manage
    serializer_class = BookSerializer           # Serializer used for validation & JSON conversion
    permission_classes = [IsAuthenticated]      # Only authenticated users can access this view