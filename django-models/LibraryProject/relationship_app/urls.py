from django.urls import path
from . import views
from .views import list_books, LibraryDetailView
urlpatterns = [
    path("", views.index, name="index"),
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail")
]