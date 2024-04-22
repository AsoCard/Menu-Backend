from django.db import models
from coffeeshop.common.models import BaseModel
from coffeeshop.product.models import Product
from coffeeshop.users.models import BaseUser
# Create your models here.


class Order(BaseModel):
    STATUS_CHOICES = (
        ('1', 'ثبت شده'),
        ('2', 'در حال آماده سازی'),
        ('3', 'آماده'),
        ('4', 'تحویل داده شده'),
    )
    address = models.CharField(
        max_length=1000
    )
    user = models.ForeignKey(
        BaseUser, on_delete=models.CASCADE
    )
    orders = models.ManyToManyField(
        to=Product
    )
    status = models.CharField(
        choices=STATUS_CHOICES
    )
    des = models.TextField()
