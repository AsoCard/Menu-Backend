from django.urls import path, include
from .apis import MenuApi
urlpatterns = [
    path('', MenuApi.as_view(), name="menu"),
]
