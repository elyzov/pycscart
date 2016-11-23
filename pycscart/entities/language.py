from .base import CSCartResource


class CSCartLanguage(CSCartResource):

    def __init__(
        self, lang_id=None, lang_code=None, name=None, status=None,
        country_code=None, direction=None
    ):

        self.lang_id = lang_id
        self.lang_code = lang_code
        self.name = name
        self.status = status
        self.country_code = country_code
        self.direction = direction
