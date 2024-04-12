from django.urls import path
from .apis import ProductApi

urlpatterns = [
    path('products/', ProductApi.as_view(), name="products"),
]
