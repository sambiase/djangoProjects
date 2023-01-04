from django.db import models


class Countries(models.Model):
    country_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=50)

    def __str__(self):
        return self.country_name
    