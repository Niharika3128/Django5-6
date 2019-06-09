from django.db import models

class Reporter(models.Model):
    name = models.CharField(primary_key=True,max_length=30)

    # def __str__(self):
    #     return self.name

class Article(models.Model):
    title = models.CharField(primary_key=True,max_length=50)
    reporter = models.ForeignKey(Reporter,on_delete=models.CASCADE)

