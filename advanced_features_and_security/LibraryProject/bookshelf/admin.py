from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    # Fields to display in the admin list view
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_superuser")

    # Fields to filter in the right sidebar
    list_filter = ("is_staff", "is_superuser", "is_active")

    # How the fields are grouped in the edit page
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

    # Fields to show when creating a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'author', 'published_date')
    list_filter = ('title', 'author', 'published_date')
    publication_year = ('published_date')

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)