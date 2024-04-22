from django.urls import path, include
from .apis import OrderApi, BartenderOrdersApi

urlpatterns = [
    path('create/', OrderApi.as_view(), name="create-order"),
    path('bartender/', BartenderOrdersApi.as_view(), name="bartender-orders")
]
