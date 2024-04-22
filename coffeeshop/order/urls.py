from django.urls import path, include
from .apis import OrderApi

urlpatterns = [
    path('create/', OrderApi.as_view(), name="create-order"),
]
