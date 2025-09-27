from rest_framework import generics, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend

# -----------------------------------------------------------------------------
# LIST VIEW
# -----------------------------------------------------------------------------
# Purpose:
#   - Returns a list of all Book objects.
# Access Control:
#   - Anyone can view (read-only).
#   - Write operations are restricted to authenticated users, though this
#     view itself only supports GET.
# Extensions:
#   - Uses IsAuthenticatedOrReadOnly to enforce read-only for anonymous users.
class BookListView(generics.ListAPIView):
    """
    BookListView:
    - Provides a list of all books.
    - Supports filtering by title, author, and publication_year.
    - Supports search on title and author.
    - Supports ordering by title and publication_year.
    - Permissions: Read for all, write only if logged in (handled in other views).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering fields
    filterset_fields = ["title", "author", "publication_year"]

    # Search fields
    search_fields = ["title", "author"]

    # Ordering fields
    ordering_fields = ["title", "publication_year"]

    # Default ordering
    ordering = ["title"]


# -----------------------------------------------------------------------------
# DETAIL VIEW
# -----------------------------------------------------------------------------
# Purpose:
#   - Retrieve a single Book instance by its primary key (id).
# Access Control:
#   - Anyone can view (read-only).
#   - Write operations are restricted by serializer and permission settings.
# Extensions:
#   - Uses IsAuthenticatedOrReadOnly so only authenticated users could perform
#     unsafe operations (if allowed in future).
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# -----------------------------------------------------------------------------
# CREATE VIEW
# -----------------------------------------------------------------------------
# Purpose:
#   - Allows creation of new Book entries.
# Access Control:
#   - Restricted to authenticated users.
# Extensions:
#   - Can override perform_create() if we want to attach request.user
#     or enforce additional validation.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# -----------------------------------------------------------------------------
# UPDATE VIEW
# -----------------------------------------------------------------------------
# Purpose:
#   - Updates an existing Book entry.
#   - Book ID is passed in the request body (request.data["id"]).
# Access Control:
#   - Restricted to authenticated users.
# Extensions:
#   - Overrides put() and patch() for full and partial updates.
#   - Returns custom error messages if ID is missing or invalid.
class BookUpdateView(generics.GenericAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        """Full update (all fields required)."""
        book_id = request.data.get("id")
        if not book_id:
            return Response({"error": "Book ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(book, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        """Partial update (only provided fields updated)."""
        book_id = request.data.get("id")
        if not book_id:
            return Response({"error": "Book ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -----------------------------------------------------------------------------
# DELETE VIEW
# -----------------------------------------------------------------------------
# Purpose:
#   - Deletes an existing Book entry.
#   - Book ID is passed in the request body (request.data["id"]).
# Access Control:
#   - Restricted to authenticated users.
# Extensions:
#   - Returns custom error messages if ID is missing or invalid.
#   - Returns a 204 response with a success message on deletion.
class BookDeleteView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        book_id = request.data.get("id")
        if not book_id:
            return Response({"error": "Book ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

        book.delete()
        return Response({"message": "Book deleted successfully."}, status=status.HTTP_204_NO_CONTENT)