from django.db import models

# Create your models here.

from employees.models import Employee

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performances')
    rating = models.IntegerField()
    review_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - {self.rating} on {self.review_date}"
