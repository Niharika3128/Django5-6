
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=30)
    salary = models.DecimalField(max_digits=10,decimal_places=2)

