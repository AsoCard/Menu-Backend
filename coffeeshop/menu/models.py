from django.db import models
from coffeeshop.common.models import BaseModel


# Create your models here.

class Menu(BaseModel):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField('product.Product')
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"
