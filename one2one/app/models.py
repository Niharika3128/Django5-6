from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField()

    def __str__(self):
        return self.name

class Hotel(models.Model):
    place = models.OneToOneField(Place,on_delete=models.CASCADE)
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)


