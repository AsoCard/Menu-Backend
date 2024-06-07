from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from coffeeshop.menu.models import Menu
from coffeeshop.menu.selectors import get_menu
from coffeeshop.product.serializers import ProductsSerializer
from coffeeshop.product.models import Product
from rest_framework import generics
from django.shortcuts import get_object_or_404


class MenuOutPutSerializer(serializers.ModelSerializer):
    products = ProductsSerializer(many=True)

    class Meta:
        model = Menu
        fields = "__all__"
\

class MenuApi(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuOutPutSerializer

    def get_object(self):
        name = self.request.GET.get('filter')
        obj = get_object_or_404(Menu, name=name)
        self.check_object_permissions(self.request, obj)
        return obj
