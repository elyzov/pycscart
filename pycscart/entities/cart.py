from .base import CSCartResource


class CSCartCart(CSCartResource):

    def __init__(
        self, user_id=None, firstname=None, lastname=None, date=None,
        ip_address=None, company_id=None, cart_products=None, total=None,
        order_id=None, user_data=[]
    ):

        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.date = date
        self.ip_address = ip_address
        self.company_id = company_id
        self.cart_products = cart_products
        self.total = total
        self.order_id = order_id
        self.user_data = user_data
