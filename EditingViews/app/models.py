from django.db import models

class Employee(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    contactno = models.IntegerField()
    email = models.EmailField(max_length=100)
    salary = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    doj = models.DateField(default=None)

