from django.urls import path
from .views import list_books, LibraryDetailView, register
#from .users_views import admin_view, librarian_view, member_view
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path("register/", views.register.as_view(), name="register"),
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
    path("accounts/profile/", views.role_based_redirect),
]