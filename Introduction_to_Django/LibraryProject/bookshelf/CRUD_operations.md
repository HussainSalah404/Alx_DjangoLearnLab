## 📄 `CRUD_operations.md`
```markdown
# CRUD Operations Documentation

This file documents the Create, Retrieve, Update, and Delete operations
performed on the `Book` model in the Django shell.

---

## Create
```python
from book_store.models import Book
book = Book.objects.create(title="1984", author="George Orwell", published_date=1949)
print(book)
Output:

csharp
Copy code
1984 by George Orwell (1949)