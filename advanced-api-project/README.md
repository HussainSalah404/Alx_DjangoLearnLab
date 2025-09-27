# Advanced API Project

This project is a **Django REST Framework (DRF) API** for managing books.  
It demonstrates CRUD operations, role-based permissions, and advanced query capabilities such as **filtering, searching, and ordering**.

---

## Features

- **CRUD for Books**
  - List all books
  - Retrieve details of a book
  - Create a book (authenticated users only)
  - Update a book (authenticated users only, requires book ID in request body)
  - Delete a book (authenticated users only, requires book ID in request body)
- **Permissions**
  - Unauthenticated users: Read-only access (list & detail views).
  - Authenticated users: Full access (create, update, delete).
- **Advanced Queries**
  - **Filtering** by title, author, and publication_year
  - **Search** by title and author
  - **Ordering** by title or publication_year

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/advanced_api_project.git
   cd advanced_api_project