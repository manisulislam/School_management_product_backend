from django.db import models
from students import Student
# Create your models here.
class BusRoute(models.Model):
    route_name = models.CharField(max_length=100)
    driver_name = models.CharField(max_length=100)
    driver_phone = models.CharField(max_length=15)
    bus_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.route_name


class BusAssignment(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    route = models.ForeignKey("BusRoute", on_delete=models.CASCADE)
    pickup_point = models.CharField(max_length=100)
