from .base import CSCartResource


class CSCartSetting(CSCartResource):

    def __init__(
        self, name=None, description=None, object_id=None, section_id=None,
        section_tab_id=None, value=None, edition_type=None, handler=None,
        is_global=None, object_type=None, position=None, section_name=None,
        section_tab_name=None, tooltip=None, type=None, variants=None,
        parent_id=None, **kwargs
    ):

        self.name = name
        self.description = description
        self.object_id = object_id
        self.section_id = section_id
        self.section_tab_id = section_tab_id
        self.value = value
        self.edition_type = edition_type
        self.handler = handler
        self.is_global = is_global
        self.object_type = object_type
        self.position = position
        self.section_name = section_name
        self.section_tab_name = section_tab_name
        self.tooltip = tooltip
        self.type = type
        self.variants = variants
        self.parent_id = parent_id

        for k, v in kwargs.items():
            setattr(self, k, v)
