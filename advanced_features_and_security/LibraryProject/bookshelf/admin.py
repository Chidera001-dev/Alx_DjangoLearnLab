from django.contrib import admin

from .models import Book



# Custom admin configuration for the Book model
class BookAdmin(admin.ModelAdmin):
    # Columns that will be shown in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Sidebar filters for easy filtering
    list_filter = ('publication_year', 'author')
    
    # Adds a search bar for these fields
    search_fields = ('title', 'author')

# Register the model with the custom admin
admin.site.register(Book, BookAdmin)




# Register your models here.
