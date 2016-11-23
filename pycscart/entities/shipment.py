from .base import CSCartResource


class CSCartShipment(CSCartResource):

    def __init__(
        self, carrier=None, order_id=None, products=None, shipping=None,
        shipping_id=None, user_id=None, tracking_number=None, comments=None,
        group_key=None, order_timestamp=None, **kwargs
    ):

        self.carrier = carrier
        self.order_id = order_id
        self.products = products
        self.shipping = shipping
        self.shipping_id = shipping_id
        self.user_id = user_id
        self.tracking_number = tracking_number
        self.comments = comments
        self.group_key = group_key
        self.order_timestamp = order_timestamp

        for k, v in kwargs.items():
            setattr(self, k, v)


class CSCartShipping(CSCartResource):

    def __init__(
        self, status=None, delivery_time=None, shipping_id=None, min_weight=None,
        shipping=None, position=None, usergroups_ids=None, max_weight=None,
        **kwargs
    ):

        self.status = status
        self.delivery_time = delivery_time
        self.shipping_id = shipping_id
        self.min_weight = min_weight
        self.shipping = shipping
        self.position = position
        self.usergroups_ids = usergroups_ids
        self.max_weight = max_weight

        for k, v in kwargs.items():
            setattr(self, k, v)
