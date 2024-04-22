from coffeeshop.order.models import Order
from coffeeshop.users.models import BaseUser


def create_order(address: str, orders: [int], des: str, user: BaseUser) -> Order:
    order = Order.objects.create(address=address, des=des, user=user)
    order.orders.set(orders)
    order.save()
    return order
