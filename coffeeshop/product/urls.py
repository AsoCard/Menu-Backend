from django.urls import path
from .apis import ProductsSearchApi, ProductDetailApi

urlpatterns = [
    path('', ProductsSearchApi.as_view(), name='product-search'),
    path('<int:pk>/', ProductDetailApi.as_view(), name='product-detail')
]
