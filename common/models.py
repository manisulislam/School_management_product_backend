from django.db import models
from users import Staff
from students import students
# Create your models here.
class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    purchase_date = models.DateField(blank=True, null=True)
    assigned_to = models.ForeignKey("Staff", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.item_name

class HealthRecord(models.Model):
    student = models.OneToOneField("Student", on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=5)
    allergies = models.TextField(blank=True, null=True)
    medical_conditions = models.TextField(blank=True, null=True)
    emergency_contact = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.student} - Health Record"
