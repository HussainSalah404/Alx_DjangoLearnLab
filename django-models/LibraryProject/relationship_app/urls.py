from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from views import Register

urlpatterns = [
    path("", views.index, name="index"),
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', Register.as_view(), name='register'),
]