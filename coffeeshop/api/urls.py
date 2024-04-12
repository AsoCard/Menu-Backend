from django.urls import path, include

urlpatterns = [
    path('auth/', include(('coffeeshop.authentication.urls', 'auth'))),
    path('products/', include(('coffeeshop.product.urls', 'product'))),
    path('menus/', include(('coffeeshop.menu.urls', 'menu'))),
]
