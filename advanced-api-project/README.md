# Advanced API Project

This project is a **Django REST Framework (DRF)** API for managing books.  
It demonstrates the use of **generic class-based views**, **custom update/delete logic**, and **DRF permissions** to restrict access based on authentication.

---

## Features

- **List all books** (public, read-only for unauthenticated users).
- **Retrieve book details** (public, read-only for unauthenticated users).
- **Create new books** (authenticated users only).
- **Update books** (authenticated users only, requires book ID).
- **Delete books** (authenticated users only, requires book ID).
- Clear separation of permissions using DRF's built-in classes:
  - `IsAuthenticatedOrReadOnly`
  - `IsAuthenticated`

---

## API Endpoints

### 1. List Books
**Endpoint:**  
```http
GET /api/books/