from django.db import models

# Create your models here.
class Hostel(models.Model):
    name = models.CharField(max_length=100)
    warden_name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Room(models.Model):
    hostel = models.ForeignKey("Hostel", on_delete=models.CASCADE)
    room_number = models.CharField(max_length=20)
    capacity = models.IntegerField()
    students = models.ManyToManyField("students.Student", blank=True)

    def __str__(self):
        return f"{self.hostel.name} - {self.room_number}"
