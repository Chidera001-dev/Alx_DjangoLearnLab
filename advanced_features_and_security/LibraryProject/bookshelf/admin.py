

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

from .models import Book



# Custom admin configuration for the Book model
class BookAdmin(admin.ModelAdmin):
    # Columns that will be shown in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Sidebar filters for easy filtering
    list_filter = ('publication_year', 'author')
    
    # Adds a search bar for these fields
    search_fields = ('title', 'author')



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)


# Register the model with the custom admin
admin.site.register(Book, BookAdmin)




# Register your models here.
