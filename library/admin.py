from django.contrib import admin
from .models import Book, BookIssue

# ✅ Register Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "isbn", "quantity")
    search_fields = ("title", "author", "isbn")
    list_filter = ("author",)

# ✅ Register BookIssue
@admin.register(BookIssue)
class BookIssueAdmin(admin.ModelAdmin):
    list_display = ("book", "student", "issue_date", "return_date", "is_returned")
    search_fields = ("book__title", "student__first_name", "student__last_name")
    list_filter = ("is_returned", "issue_date", "return_date")
