from django.db import models

# Create your models here.

class Anomaly(models.Model):
    date = models.DateField()
    data_type = models.CharField(max_length=255)
    user_score = models.IntegerField()
    algorithm_score = models.FloatField()
