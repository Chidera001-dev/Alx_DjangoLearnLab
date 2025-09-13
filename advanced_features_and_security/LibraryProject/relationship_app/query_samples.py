# relationship_app/query_samples.py
import os
import django

# 1) tell Django which settings to load - change 'LibraryProject.settings' to your project settings path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


# 1. Query all books by a specific author
author_name = "John Doe"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}:", books_by_author)

# 2. List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)   
books_in_library = library.books.all()
print(f"Books in {library_name}:", books_in_library)

# 3. Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"Librarian for {library_name}:", librarian.name)


