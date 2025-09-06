from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required
from .models import Book
from .models import Library


# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view: detail of a single library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# User registration view
def register(request):  # use 'register' to match urls.py
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# User login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("list_books")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})


# User logout view
def logout_view(request):
    auth_logout(request)
    return render(request, "relationship_app/logout.html")


# helper to check role safely
def has_role(role_name):
    def check(user):
        # check user is authenticated and has userprofile with the role
        if not user.is_authenticated:
            return False
        profile = getattr(user, "userprofile", None)
        return profile is not None and profile.role == role_name
    return check

# NOTE the decorator order below ensures login is checked first
@user_passes_test(has_role('Admin'), login_url='login')
@login_required(login_url='login')
def admin_view(request):
    """Only Admin users can access."""
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(has_role('Librarian'), login_url='login')
@login_required(login_url='login')
def librarian_view(request):
    """Only Librarian users can access."""
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(has_role('Member'), login_url='login')
@login_required(login_url='login')
def member_view(request):
    """Only Member users can access."""
    return render(request, "relationship_app/member_view.html")



@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    # logic to add a book
    pass

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    # logic to edit a book
    pass

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    # logic to delete a book
    pass



