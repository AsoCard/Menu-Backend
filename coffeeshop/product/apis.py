from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework import serializers, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from coffeeshop.product.models import Product, Recepie
from coffeeshop.product.selectors import get_products
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework import generics
from .serializers import ProductsSerializer, RecepiesSerializer


class ProductsSearchApi(generics.ListAPIView):
    queryset = Product.objects.all()
    filter_backends = [filters.SearchFilter]
    serializer_class = ProductsSerializer
    search_fields = ['name', 'detail', 'category__name']


class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    search_fields = ['name', 'detail', 'category__name']


class RecepieDetailApi(APIView):

    def get(self, request, pk):
        recepies = Recepie.objects.filter(product__id=pk)
        if not recepies.exists():
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = RecepiesSerializer(recepies[0])
        return Response(serializer.data, status=status.HTTP_200_OK)
