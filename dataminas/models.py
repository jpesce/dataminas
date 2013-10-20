from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    name_url = models.CharField(max_length=255)
    parent = models.ForeignKey('self')

class Point(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    value = models.IntegerField()
    category = models.ForeignKey('Category')
    user_score = models.IntegerField()
    algorithm_score = models.IntegerField()
