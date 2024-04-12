from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from coffeeshop.menu.models import Menu
from coffeeshop.menu.selectors import get_menu
from coffeeshop.product.serializers import ProductsSerializer


class MenuApi(APIView):
    class MenuOutPutSerializer(serializers.ModelSerializer):
        products = ProductsSerializer(many=True)

        class Meta:
            model = Menu
            fields = "__all__"

    @extend_schema(responses=MenuOutPutSerializer)
    def get(self, request):
        query = get_menu()
        return Response(self.MenuOutPutSerializer(query, context={"request": request}).data)
