from django.urls import path
from .apis import ProductsSearchApi, ProductDetailApi, RecepieDetailApi

urlpatterns = [
    path('', ProductsSearchApi.as_view(), name='product-search'),
    path('<int:pk>/', ProductDetailApi.as_view(), name='product-detail'),
    path('recepie/<int:pk>', RecepieDetailApi.as_view(), name='recepie-detail')
]
