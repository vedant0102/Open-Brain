from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0) #cents





# Create your models here.
