from .base import CSCartResource


class CSCartStatus(CSCartResource):

    def __init__(
        self, status=None, description=None, status_id=None, email_header=None,
        is_default=None, params=None, email_subj=None, lang_code=None,
        type=None, **kwargs
    ):

        self.status = status
        self.description = description
        self.status_id = status_id
        self.email_header = email_header
        self.is_default = is_default
        self.params = params
        self.email_subj = email_subj
        self.lang_code = lang_code
        self.type = type

        for k, v in kwargs.items():
            setattr(self, k, v)
