# Django Blog Project

A full-featured Django blog with user authentication, CRUD posts, comments, tagging, and search functionality.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Project Structure](#project-structure)  
6. [Implementation Details](#implementation-details)  
7. [Contributing](#contributing)  
8. [License](#license)  

---

## Project Overview

A Django-based blogging platform where users can register, create posts, comment, add tags, and search posts.

---

## Features

- User registration, login, logout, and profile management  
- CRUD operations for posts  
- Comment system with edit/delete for authors  
- Tagging system for posts  
- Search posts by title, content, or tags  
- Permissions for authenticated users and authors  

---

## Installation

1. Clone the repo:

```bash
git clone https://github.com/your-username/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/django_blog
Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
Open http://127.0.0.1:8000/ in your browser.