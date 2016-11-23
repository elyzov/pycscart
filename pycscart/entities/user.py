from .base import CSCartResource


class CSCartUser(CSCartResource):

    def __init__(
        self, status=None, user_id=None, firstname=None, user_login=None,
        company=None, user_type=None, company_id=None, is_root=None,
        points=None, timestamp=None, lastname=None, email=None, **kwargs
    ):

        self.status = status
        self.user_id = user_id
        self.firstname = firstname
        self.user_login = user_login
        self.company = company
        self.user_type = user_type
        self.company_id = company_id
        self.is_root = is_root
        self.points = points
        self.timestamp = timestamp
        self.lastname = lastname
        self.email = email

        for k, v in kwargs.items():
            setattr(self, k, v)
