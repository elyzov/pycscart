from .base import CSCartResource


class CSCartUsergroup(CSCartResource):

    def __init__(
        self, status=None, usergroup_id=None, type=None, usergroup=None,
        **kwargs
    ):

        self.status = status
        self.usergroup_id = usergroup_id
        self.type = type
        self.usergroup = usergroup

        for k, v in kwargs.items():
            setattr(self, k, v)
