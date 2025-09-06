# relationship_app/query_samples.py
import os
import django

# 1) tell Django which settings to load - change 'LibraryProject.settings' to your project settings path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# ---- create sample data (safe to run multiple times with get_or_create) ----
author, _ = Author.objects.get_or_create(name="George Orwell")
book1, _  = Book.objects.get_or_create(title="1984", author=author)
book2, _  = Book.objects.get_or_create(title="Animal Farm", author=author)

library, _ = Library.objects.get_or_create(name="Central Library")
# add books to library (ManyToMany)
library.books.add(book1, book2)

librarian, _ = Librarian.objects.get_or_create(name="Jane Doe", library=library)

# ---- Queries you were asked to prepare ----

# Query all books by a specific author
books_by_orwell = Book.objects.filter(author__name="George Orwell")
print("Books by George Orwell:", [b.title for b in books_by_orwell])

# List all books in a library
books_in_library = library.books.all()
print(f"Books in {library.name}:", [b.title for b in books_in_library])

# Retrieve the librarian for a library
print(f"Librarian for {library.name}:", library.librarian.name)

# Extra: Reverse lookups using related_name
print("Books via author reverse lookup:", [b.title for b in author.books.all()])
print("Libraries containing '1984':", [lib.name for lib in book1.libraries.all()])

