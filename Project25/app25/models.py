from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    date = models.DateField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='product/')

    def __str__(self):
        return self.name

class LoginDetails(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)