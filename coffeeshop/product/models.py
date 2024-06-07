from django.db import models
from coffeeshop.common.models import BaseModel


# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Image(BaseModel):
    image = models.ImageField(upload_to='product/images/')

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"


class Product(BaseModel):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=1000)
    price = models.FloatField()
    ingredients = models.CharField(max_length=1000)
    images = models.ManyToManyField(Image)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Recepie(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    ingredients  = models.TextField(null=True, blank=True)
    steps = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='recepie/', null=True, blank=True)
    video = models.FileField(null=True, blank=True)


    def __str__(self):
        return self.title