from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("teacher", "Teacher"),
        ("student", "Student"),
        ("staff", "Staff"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="student")

    def __str__(self):
        return f"{self.username} ({self.role})"

class Staff(models.Model):
    staff_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)  # e.g. Clerk, Librarian
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    hire_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.role}"


