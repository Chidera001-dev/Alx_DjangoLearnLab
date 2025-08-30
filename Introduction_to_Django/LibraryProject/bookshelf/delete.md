from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Delete the book
book.delete()
# Output: (1, {'bookshelf.Book': 1})

# Confirm deletion
Book.objects.all()
# Output: <QuerySet []>

