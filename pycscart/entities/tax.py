from .base import CSCartResource


class CSCartTax(CSCartResource):

    def __init__(
        self, status=None, display_including_tax=None, tax=None,
        price_includes_tax=None, priority=None, regnumber=None,
        address_type=None, tax_id=None, **kwargs
    ):

        self.status = status
        self.display_including_tax = display_including_tax
        self.tax = tax
        self.price_includes_tax = price_includes_tax
        self.priority = priority
        self.regnumber = regnumber
        self.address_type = address_type
        self.tax_id = tax_id

        for k, v in kwargs.items():
            setattr(self, k, v)
