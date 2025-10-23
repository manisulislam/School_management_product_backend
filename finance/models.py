from django.db import models
from students import Student
# Create your models here.
class Fee(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.student} - {self.amount}"
