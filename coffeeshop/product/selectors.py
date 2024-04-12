from .models import Product


def get_products() -> [Product]:
    return Product.objects.all()
