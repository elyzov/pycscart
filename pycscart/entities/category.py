from .base import CSCartResource


class CSCartCategory(CSCartResource):

    def __init__(
        self, category=None, company_id=None, status=None, age_limit=None,
        age_verification=None, age_warning_message=None, category_id=None,
        default_layout=None, description=None, id_path=None, lang_code=None,
        localization=None, main_pair=None, meta_description=None,
        meta_keywords=None, page_title=None, parent_age_limit=None,
        parent_age_verification=None, parent_id=None, position=None,
        product_columns=None, product_count=None, product_details_layout=None,
        selected_layouts=None, seo_name=None, seo_path=None, timestamp=None,
        usergroups_ids=None
    ):

        self.category = category
        self.company_id = company_id
        self.age_limit = age_limit
        self.age_verification = age_verification
        self.age_warning_message = age_warning_message
        self.category_id = category_id
        self.default_layout = default_layout
        self.description = description
        self.id_path = id_path
        self.lang_code = lang_code
        self.localization = localization
        self.main_pair = main_pair
        self.meta_description = meta_description
        self.meta_keywords = meta_keywords
        self.page_title = page_title
        self.parent_age_limit = parent_age_limit
        self.parent_age_verification = parent_age_verification
        self.parent_id = parent_id,
        self.position = position
        self.product_columns = product_columns
        self.product_count = product_count
        self.product_details_layout = product_details_layout
        self.selected_layouts = selected_layouts
        self.seo_name = seo_name
        self.timestamp = timestamp
        self.usergroups_ids = usergroups_ids
