from django.db import models

# Create your models here.

class Point(models.Model):
    x = models.DateField()
    y = models.DecimalField(max_digits=32, decimal_places=2)
