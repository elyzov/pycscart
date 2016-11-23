from .base import CSCartResource


class CSCartStore(CSCartResource):

    def __init__(
        self, status=None, secure_storefront=None, timestamp=None,
        company_id=None, storefront=None, company_thread_ids=None,
        lang_code=None, email=None, **kwargs
    ):

        self.status = status
        self.secure_storefront = secure_storefront
        self.timestamp = timestamp
        self.company_id = company_id
        self.storefront = storefront
        self.company_thread_ids = company_thread_ids
        self.lang_code = lang_code
        self.email = email

        for k, v in kwargs.items():
            setattr(self, k, v)
