# Create Operation

**Command:**
```python
from book_store.models import Book
book = Book.objects.create(title="1984", author="George Orwell", published_date=1949)
print(book)
Expected Output:

csharp
Copy code
1984 by George Orwell (1949)