from django.db import models
from django.db import models

# Author model represents a book author.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book model represents a book with title, year, and author.
# One-to-many relationship: Author -> Books.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name="books",  # allows author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


# Create your models here.
