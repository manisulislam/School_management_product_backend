from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Staff

# ✅ Custom UserAdmin
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "role", "is_active", "is_staff", "is_superuser")
    list_filter = ("role", "is_staff", "is_superuser", "is_active")
    search_fields = ("username", "email")
    ordering = ("username",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Permissions", {"fields": ("role", "is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "role", "password1", "password2"),
        }),
    )

# ✅ Register Staff
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("staff_id", "name", "role", "phone", "email", "hire_date")
    search_fields = ("staff_id", "name", "role", "email")
    list_filter = ("role", "hire_date")
    ordering = ("name",)
