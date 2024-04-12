from rest_framework import serializers

from coffeeshop.product.models import Product, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name")
    images = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"