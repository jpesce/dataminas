from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    name_url = models.CharField(max_length=255)
    parent = models.ForeignKey('Category', blank=True, null=True, default=None)

class Point(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    value = models.DecimalField(max_digits=32, decimal_places=2)
    category = models.ForeignKey('Category')
    user_score = models.IntegerField()
    algorithm_score = models.IntegerField()
