from django.contrib import admin
from .models import Student, Teacher

# ✅ Register Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "student_id",
        "first_name",
        "last_name",
        "class_assigned",
        "dob",
        "gender",
        "admission_date",
        "guardian_name",
    )
    search_fields = ("first_name", "last_name", "student_id", "guardian_name")
    list_filter = ("class_assigned", "gender", "admission_date")
    ordering = ("first_name", "last_name")

# ✅ Register Teacher
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("teacher_id", "name", "specialization", "dob", "email", "phone", "hire_date")
    search_fields = ("name", "teacher_id", "specialization", "email")
    list_filter = ("specialization", "hire_date")
    ordering = ("name",)
