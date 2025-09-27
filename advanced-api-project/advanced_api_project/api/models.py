from django.db import models
import datetime

# The Author model represents a book author.
# Each Author can have multiple Books related to them (one-to-many relationship).
class Author(models.Model):
    name = models.CharField(max_length=100)  # Name of the author

    def __str__(self):
        return self.name


# The Book model represents a single book in the system.
# Each Book belongs to one Author (ForeignKey relationship).
# related_name="books" allows us to access an author's books using author.books.all().
class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    publication_year = models.IntegerField()  # Year when the book was published
    author = models.ForeignKey(
        Author,
        related_name="books",   # Enables reverse lookup from Author -> Books
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    



# Create your models here.
