from .base import CSCartResource


class CSCartDiscussion(CSCartResource):

    def __init__(
        self, object_type=None, object_id=None, thread_id=None, name=None,
        message=None, rating_value=None, timestamp=None, status=None,
        post_id=None, user_id=None, ip_address=None, type=None, company_id=None
    ):

        self.object_type = object_type
        self.object_id = object_id
        self.thread_id = thread_id
        self.name = name
        self.message = message
        self.rating_value = rating_value
        self.timestamp = timestamp
        self.status = status
        self.post_id = post_id
        self.user_id = user_id
        self.ip_address = ip_address
        self.type = type
        self.company_id = company_id
