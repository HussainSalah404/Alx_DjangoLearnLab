## 📄 `delete.md`
```markdown
# Delete Operation

**Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

print(Book.objects.all())
Expected Output:

css
Copy code
<QuerySet []>