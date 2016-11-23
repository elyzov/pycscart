from .base import CSCartResource


class CSCartPage(CSCartResource):

    def __init__(
        self, status=None, position=None, description=None, level=None,
        timestamp=None, company_id=None, page=None, page_id=None,
        parent_id=None, new_window=None, avail_till_timestamp=None,
        page_type=None, use_avail_period=None, id_path=None, lang_code=None,
        usergroup_ids=None, avail_from_timestamp=None, **kwargs
    ):

        self.status = status
        self.position = position
        self.description = description
        self.level = level
        self.timestamp = timestamp
        self.company_id = company_id
        self.page = page
        self.page_id = page_id
        self.parent_id = parent_id
        self.new_window = new_window
        self.avail_till_timestamp = avail_till_timestamp
        self.page_type = page_type
        self.use_avail_period = use_avail_period
        self.id_path = id_path
        self.lang_code = lang_code
        self.usergroup_ids = usergroup_ids
        self.avail_from_timestamp = avail_from_timestamp

        for k, v in kwargs.items():
            setattr(self, k, v)
