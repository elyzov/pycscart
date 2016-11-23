from .base import CSCartResource


class CSCartBlock(CSCartResource):

    def __init__(
        self, block_id=None, type=None, properties=None, company_id=None,
        lang_code=None, name=None, content=None
    ):

        self.block_id = block_id
        self.type = type
        self.properties = properties
        self.company_id = company_id
        self.lang_code = lang_code
        self.name = name
        self.content = content
