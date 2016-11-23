from .base import CSCartResource


class CSCartVendor(CSCartResource):

    def __init__(
        self, company_id=None, lang_code=None, email=None, company=None,
        timestamp=None, status=None, seo_name=None, seo_path=None,
        average_rating=None, company_thread_ids=None, **kwargs
    ):

        self.company_id = company_id
        self.lang_code = lang_code
        self.email = email
        self.company = company
        self.timestamp = timestamp
        self.status = status
        self.seo_name = seo_name
        self.seo_path = seo_path
        self.average_rating = average_rating
        self.company_thread_ids = company_thread_ids
        for k, v in kwargs.items():
            setattr(self, k, v)
