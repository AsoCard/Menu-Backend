from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework import serializers, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from coffeeshop.product.models import Image, Product, Recepie
from coffeeshop.product.selectors import get_products
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework import generics
from .serializers import ProductsSerializer, RecepiesSerializer, ImageSerializer, ProductCreateSerializer


class ProductsSearchApi(generics.ListAPIView):
    queryset = Product.objects.all()
    filter_backends = [filters.SearchFilter]
    serializer_class = ProductsSerializer
    search_fields = ['name', 'detail', 'category__name']


class ProductCreateIMGApi(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class RecepieCreateApi(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Recepie.objects.all()
    serializer_class = RecepiesSerializer


class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    search_fields = ['name', 'detail', 'category__name']


class ProductCreateApi(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


class RecepieDetailApi(APIView):

    def get(self, request, pk):
        recepies = Recepie.objects.filter(product__id=pk)
        if not recepies.exists():
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = RecepiesSerializer(recepies[0])
        return Response(serializer.data, status=status.HTTP_200_OK)


class RecepieDetailActionApi(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    search_fields = ['name', 'detail', 'category__name']