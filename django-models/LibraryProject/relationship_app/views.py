from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view
def list_books(request):
    books = Book.objects.all()
    # Render the template 'relationship_app/list_books.html'
    # and pass a context where the template variable "books" = the queryset above.
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view

class LibraryDetailView(DetailView):
    model = Library                     # the model this view displays
    template_name = "relationship_app/library_detail.html"  # template to render
    context_object_name = "library"     # template variable name for the Library instance



# Create your views here.
