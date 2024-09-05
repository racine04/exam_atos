from django.db import models

# Create your models here.
class PlatModel(models.Model):
    name = models.CharField(max_length=100)
    summary= models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"