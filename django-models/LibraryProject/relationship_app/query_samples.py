from relationship_app.models import name, Library

books = Library.objects.get(name=library_name)
books.all()