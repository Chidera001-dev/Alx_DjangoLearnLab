from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Book, Library


# Function-based view (list all books)
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Class-based view (details for a specific library)
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# User registration view
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()          # create user
            auth_login(request, user)   # log in user immediately
            return redirect("list_books")  # redirect after login
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# User login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)   # log in user
            return redirect("list_books")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})


# User logout view
def logout_view(request):
    auth_logout(request)  # log out user
    return render(request, "relationship_app/logout.html")
