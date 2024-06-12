from coffeeshop.order.models import Order
from coffeeshop.users.models import BaseUser


def create_order(address: str, orders: [int], des: str, user: BaseUser, status: str, count) -> Order:
    order = Order.objects.create(address=address, des=des, user=user, status=status, count=count)
    order.orders.set(orders)
    order.save()
    return order
