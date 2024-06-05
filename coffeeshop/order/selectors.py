from coffeeshop.order.models import Order


def get_orders(status: str | None) -> [Order]:
    queryset = Order.objects.all()
    if status is not None:
        queryset = queryset.filter(status=status)
    return queryset

def update_order_status(order: Order, status: str) -> str:
    order.status = status
    order.save()
    return order.status
