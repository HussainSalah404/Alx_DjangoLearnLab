from django.urls import path
from .views import list_books, LibraryDetailView, register
from .users_views import admin_view, librarian_view, member_view
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library-detail"),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path("register/", views.register.as_view(), name="register"),
    path("admin-dashboard/", admin_view.admin_dashboard, name="admin_dashboard"),
    path("librarian-dashboard/", librarian_view.librarian_dashboard, name="librarian_dashboard"),
    path("member-dashboard/", member_view.member_dashboard, name="member_dashboard"),
    path("accounts/profile/", views.role_based_redirect),
]