from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'author', 'published_date')
    list_filter = ('title', 'author', 'published_date')
    publication_year = ('published_date')

admin.site.register(Book, BookAdmin)