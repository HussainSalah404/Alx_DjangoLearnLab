from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books-viewset', BookViewSet, basename='book')

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),   # Maps to the BookList view
    
    # Include the router URLs for BookViewSet (all CRUD operations)
    path('books_all/', include(router.urls)),  # This includes all routes registered with the router
    
]