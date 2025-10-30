from django.contrib import admin
from .models import (
    ClassRoom,
    Subject,
    Attendance,
    Exam,
    Result,
    Announcement,
    Timetable,
    Event,
)

# ✅ Register ClassRoom
@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ("name", "section", "capacity", "class_teacher")
    search_fields = ("name", "section", "class_teacher__name")
    list_filter = ("section",)

# ✅ Register Subject
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "teacher")
    search_fields = ("name", "code", "teacher__name")
    list_filter = ("teacher",)

# ✅ Register Attendance
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("student", "date", "status")
    search_fields = ("student__first_name", "student__last_name")
    list_filter = ("status", "date")

# ✅ Register Exam
@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date")
    search_fields = ("name",)
    list_filter = ("start_date", "end_date")

# ✅ Register Result
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "exam", "marks_obtained", "grade")
    search_fields = ("student__first_name", "subject__name", "exam__name")
    list_filter = ("exam", "subject", "grade")

# ✅ Register Announcement
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "created_at")
    search_fields = ("title", "created_by__name")
    list_filter = ("created_at",)

# ✅ Register Timetable
@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ("classroom", "subject", "teacher", "day_of_week", "start_time", "end_time")
    search_fields = ("classroom__name", "subject__name", "teacher__name")
    list_filter = ("day_of_week", "classroom")

# ✅ Register Event
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "start_time", "end_time")
    search_fields = ("title",)
    list_filter = ("date",)
