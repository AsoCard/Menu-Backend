from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework import serializers, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from coffeeshop.product.models import Product
from coffeeshop.product.selectors import get_products
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from .serializers import ProductsSerializer

class ProductsSearchApi(generics.ListAPIView):
    queryset = Product.objects.all()
    filter_backends = [filters.SearchFilter]
    serializer_class = ProductsSerializer
    search_fields = ['name', 'detail', 'category__name']