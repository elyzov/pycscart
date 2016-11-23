from .base import CSCartResource


class CSCartCallRequest(CSCartResource):

    def __init__(
        self, email=None, phone=None, user_id=None, order_id=None,
        product_id=None, timestamp=None, status=None, name=None,
        time_from=None, time_to=None, notes=None, cart_products=None,
        order_status=None, product=None
    ):

        self.email = email
        self.phone = phone
        self.user_id = user_id
        self.order_id = order_id
        self.product_id = product_id
        self.status = status
        self.name = name
        self.time_from = time_from
        self.time_to = time_to
        self.notes = notes
        self.cart_products = cart_products
        self.order_status = order_status
        self.product = product
