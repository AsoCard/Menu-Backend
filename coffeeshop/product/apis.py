from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from rest_framework import serializers, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from coffeeshop.product.models import Product
from coffeeshop.product.selectors import get_products


class ProductApi(APIView):
    class ProductOutPutSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = "__all__"

    @extend_schema(responses=ProductOutPutSerializer)
    def get(self, request):
        query = get_products()
        return Response(self.ProductOutPutSerializer(query, context={"request": request}, many=True).data)
