from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=[("M", "Male"), ("F", "Female")])
    address = models.TextField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    guardian_name = models.CharField(max_length=100)
    guardian_phone = models.CharField(max_length=15)
    admission_date = models.DateField(auto_now_add=True)
    class_assigned = models.ForeignKey("ClassRoom", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(models.Model):
    teacher_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    specialization = models.CharField(max_length=100)
    hire_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
