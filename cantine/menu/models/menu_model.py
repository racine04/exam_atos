from django.db import models

from plat.models.plat_model import PlatModel

# Create your models here.
class MenuModel(models.Model):
    creation_date= models.DateField(auto_now_add=True)
    plat = models.OneToOneField(PlatModel, on_delete=models.CASCADE)