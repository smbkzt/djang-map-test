from django.db import models


class MapDots(models.Model):
    name = models.CharField(blank=False, max_length=100)
    longitute = models.CharField(blank=False, max_length=100)
    latitute = models.CharField(blank=False, max_length=100)

    def __str__(self, *args, **kwargs):
        return self.name
