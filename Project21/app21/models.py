from django.db import models

class HODModel(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class FacultyModel(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=20)

class StudentModel(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    group = models.CharField(max_length=20)

class Parent(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=20)
