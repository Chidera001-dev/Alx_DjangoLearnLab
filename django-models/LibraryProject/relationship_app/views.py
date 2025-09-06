from django.shortcuts import render


from django.views.generic import DetailView
from .models import Book, Library

# Function-based view
from django.shortcuts import render
from .models import Book

def list_books(request):
    # Query: get all Book objects and also fetch their authors in the same SQL (optimization).
    books = Book.objects.select_related('author').all()
    # Render the template 'relationship_app/list_books.html'
    # and pass a context where the template variable "books" = the queryset above.
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view

class LibraryDetailView(DetailView):
    model = Library                     # the model this view displays
    template_name = "relationship_app/library_detail.html"  # template to render
    context_object_name = "library"     # template variable name for the Library instance

    # optional: add extra context (not required, but useful)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['books'] could be used, but library.books.all() is accessible from template
        return context


# Create your views here.
