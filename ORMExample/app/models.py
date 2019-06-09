from django.db import models

class Person(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    contact = models.IntegerField()
