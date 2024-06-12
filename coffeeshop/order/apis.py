from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from drf_spectacular.utils import extend_schema
from rest_framework import status, serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Order
from .services import create_order
from .selectors import get_orders, update_order_status
from ..product.serializers import ProductsSerializer
from ..users.models import BaseUser
from ..users.serializers import SmallUserSerializer


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('address', 'orders', 'status', 'des')


class OrderSerializer(serializers.ModelSerializer):
    user = SmallUserSerializer()
    orders = ProductsSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderApi(APIView):
    permission_classes = [AllowAny]

    @extend_schema(request=CreateOrderSerializer, responses=CreateOrderSerializer)
    def post(self, request):
        serializer = CreateOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = create_order(
                address=serializer.validated_data.get("address"),
                orders=serializer.validated_data.get("orders"),
                status=serializer.validated_data.get("status"),
                des=serializer.validated_data.get("des"),
                user=request.user
            )
        except Exception as ex:
            return Response(
                f"Database Error {ex}",
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(CreateOrderSerializer(user, context={"request": request}).data)


class BartenderOrdersApi(APIView):
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['status']

    @extend_schema(responses=OrderSerializer)
    def get(self, request):
        status = request.query_params.get('status')
        query = get_orders(status=status)
        return Response(OrderSerializer(query, context={"request": request}, many=True).data)
    
    @extend_schema(responses=OrderSerializer)
    def put(self, request):
        order_id = request.query_params.get('id')
        status = request.data.get('status')
        order = get_object_or_404(Order, id=order_id)
        query = update_order_status(order=order, status=status)
        return Response({
            "status": "با موفقیت ویرایش شد."
        })
