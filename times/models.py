from django.db import models

class Times(models.Model):
    time = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
