from django.contrib import admin
from .models import Fee

# ✅ Register Fee
@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ("student", "amount", "due_date", "is_paid", "payment_date")
    search_fields = ("student__first_name", "student__last_name")
    list_filter = ("is_paid", "due_date")
    ordering = ("due_date",)
