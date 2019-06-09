from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Student(models.Model):
    idno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    join_course = models.ManyToManyField(Course)
    doj = models.DateField(auto_now_add=True)


