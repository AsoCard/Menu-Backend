from django.urls import path, include

urlpatterns = [
    path('auth/', include(('coffeeshop.authentication.urls', 'auth'))),
]
