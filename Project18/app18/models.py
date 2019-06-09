from django.db import models

class Usermodel(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='user_images/')
