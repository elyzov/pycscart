from .base import CSCartResource


class CSCartLangvar(CSCartResource):

    def __init__(self, name=None, value=None):

        self.name = name
        self.value = value
