from django.db import models
from coffeeshop.common.models import BaseModel


# Create your models here.
class Product(BaseModel):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=1000)
    price = models.FloatField()
    ingredients = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
