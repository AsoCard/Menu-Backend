from drf_spectacular.utils import extend_schema
from rest_framework import status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .services import create_order


class OrderApi(APIView):
    permission_classes = [IsAuthenticated]

    class CreateOrderSerializer(serializers.ModelSerializer):
        class Meta:
            model = Order
            fields = ('address', 'orders', 'des')

    @extend_schema(request=CreateOrderSerializer, responses=CreateOrderSerializer)
    def post(self, request):
        serializer = self.CreateOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = create_order(
                address=serializer.validated_data.get("address"),
                orders=serializer.validated_data.get("orders"),
                des=serializer.validated_data.get("des"),
                user=request.user
            )
        except Exception as ex:
            return Response(
                f"Database Error {ex}",
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(self.CreateOrderSerializer(user, context={"request": request}).data)
