from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    powerPoins = models.IntegerField()

    def __str__(self) -> str:
        return self.name
        