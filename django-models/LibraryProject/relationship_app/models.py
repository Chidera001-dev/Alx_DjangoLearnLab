# relationship_app/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=150)
    books = models.ManyToManyField(
        Book,
        related_name='libraries',
        blank=True
    )

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(
        Library,
        on_delete=models.CASCADE,
        related_name='librarian'
    )

    def __str__(self):
        return f"{self.name} ({self.library.name})"




class UserProfile(models.Model):
    ROLE_ADMIN = 'Admin'
    ROLE_LIBRARIAN = 'Librarian'
    ROLE_MEMBER = 'Member'

    ROLE_CHOICES = [
        (ROLE_ADMIN, 'Admin'),
        (ROLE_LIBRARIAN, 'Librarian'),
        (ROLE_MEMBER, 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_MEMBER)

    def __str__(self):
        return f"{self.user.username} ({self.role})"


@receiver(post_save, sender=User)
def create_or_update_userprofile(sender, instance, created, **kwargs):
    """
    When a User is created, create a UserProfile.
    If user already exists ensure a profile exists (safe-guard).
    """
    if created:
        UserProfile.objects.create(user=instance)
    else:
        # if profile missing for some reason, create it
        try:
            instance.userprofile.save()
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(user=instance)




class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    class Meta:
        permissions = (
            ("can_add_book", "Can add a new book"),
            ("can_change_book", "Can edit a book"),
            ("can_delete_book", "Can delete a book"),
        )

    def __str__(self):
        return self.title



# Create your models here.
