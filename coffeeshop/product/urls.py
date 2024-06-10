from django.urls import path
from .apis import ProductsSearchApi, ProductDetailApi, RecepieDetailApi, ProductCreateApi, ProductCreateIMGApi

urlpatterns = [
    path('', ProductsSearchApi.as_view(), name='product-search'),
    path("add/", ProductCreateApi.as_view(), name="product-add"),
    path("img-add/", ProductCreateIMGApi.as_view(), name="product-add"),
    path('<int:pk>/', ProductDetailApi.as_view(), name='product-detail'),
    path('recepie/<int:pk>', RecepieDetailApi.as_view(), name='recepie-detail')
]
