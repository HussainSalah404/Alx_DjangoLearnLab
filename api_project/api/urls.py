from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books-viewset', BookViewSet, basename='book')

urlpatterns = [
    
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),   # Maps to the BookList view
    
    # Include the router URLs for BookViewSet (all CRUD operations)
    path('books_all/', include(router.urls)),  # This includes all routes registered with the router
    
    # Route for obtaining an auth token (login using username & password -> returns token)
    path('auth/token/', obtain_auth_token, name='api_token_auth'), # Used for token-based authentication

]