from django.contrib import admin
from .models import Product, Category, Image, Recepie
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Recepie)
