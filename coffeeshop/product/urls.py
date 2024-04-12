from django.urls import path
from .apis import ProductApi

urlpatterns = [
    path('', ProductApi.as_view(), name="products"),
]
