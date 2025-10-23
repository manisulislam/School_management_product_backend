from django.db import models
from students import Teacher, Student
# Create your models here.

class ClassRoom(models.Model):
    name = models.CharField(max_length=20)  # e.g. "Grade 10 - A"
    section = models.CharField(max_length=5, blank=True, null=True)
    capacity = models.IntegerField(default=40)
    class_teacher = models.ForeignKey("Teacher", on_delete=models.SET_NULL, null=True, related_name="classroom_teacher")

    def __str__(self):
        return self.name


class Subject(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey("Teacher", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[("Present", "Present"), ("Absent", "Absent"), ("Leave", "Leave")])

    class Meta:
        unique_together = ("student", "date")


class Exam(models.Model):
    name = models.CharField(max_length=100)  # e.g. "Midterm 2025"
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Result(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE)
    exam = models.ForeignKey("Exam", on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=2)

    class Meta:
        unique_together = ("student", "subject", "exam")


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey("Teacher", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class Timetable(models.Model):
    classroom = models.ForeignKey("ClassRoom", on_delete=models.CASCADE)
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE)
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, choices=[
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
        ("Friday", "Friday"),
        ("Saturday", "Saturday"),
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ("classroom", "day_of_week", "start_time")

    def __str__(self):
        return f"{self.classroom} - {self.subject}"


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.title
