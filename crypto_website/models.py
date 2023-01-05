from django.db import models


class CryptoModel(models.Model):
    logo = models.URLField()
    name = models.CharField(max_length=50)
    rank = models.CharField(max_length=50)
    marketcap = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.name
