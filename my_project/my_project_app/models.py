from django.db import models

# Create your models here.
class Categories(models.Model):
    category=models.CharField(max_length=250)
    description=models.CharField(max_length=1050)
    