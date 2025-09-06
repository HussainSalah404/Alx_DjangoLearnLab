from relationship_app.models import name, Library, Author, Book

books = Library.objects.get(name=library_name)
books.all()

author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
