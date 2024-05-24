from django.urls import path
from .apis import ProductApi, ProductsSearchApi

urlpatterns = [
    path('', ProductApi.as_view(), name="products"),
    path('search/', ProductsSearchApi.as_view(), name='product-search'),
]
