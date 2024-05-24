from django.urls import path
from .apis import ProductsSearchApi

urlpatterns = [
    path('', ProductsSearchApi.as_view(), name='product-search'),
]
