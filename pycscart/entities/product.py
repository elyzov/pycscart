from .base import CSCartResource


class CSCartProductMainPair(CSCartResource):

    def __init__(
        self, detailed=None, image_id=None, detailed_id=None, pair_id=None,
        position=None, **kwargs
    ):

        self.detailed = detailed
        self.image_id = image_id
        self.detailed_id = detailed_id
        self.pair_id = pair_id
        self.position = position

        for k, v in kwargs.items():
            setattr(self, k, v)


class CSCartProductImagePair(CSCartResource):

    def __init__(
        self, detailed_id=None, image_id=None, detailed=None,
        pair_id=None, position=None, **kwargs
    ):

        self.detailed_id = detailed_id
        self.image_id = image_id
        self.detailed = detailed
        self.pair_id = pair_id
        self.position = position

        for k, v in kwargs.items():
            setattr(self, k, v)


class CSCartProduct(CSCartResource):

    def __init__(
        self, list_price=None, weight=None, out_of_stock_actions=None,
        is_oper=None, age_verification=None, height=None, is_pbp=None,
        unlimited_download=None, exceptions_type=None, is_op=None,
        updated_timestamp=None, free_shipping=None, product_code=None,
        avail_since=None, main_category=None, discussion_type=None,
        shipping_freight=None, company_id=None, edp_shipping=None,
        category_ids=None, discounts=None, low_avail_limit=None,
        details_layout=None, main_pair=None, age_limit=None, tax_ids=None,
        status=None, product=None, shipping_params=None, timestamp=None,
        price=None, product_features=None, product_options=None,
        product_combinations=None, options_type=None, max_qty=None,
        min_qty=None, return_period=None, zero_price_action=None, qty_step=None,
        tracking=None, product_type=None, product_id=None, list_qty_count=None,
        usergroup_ids=None, is_edp=None, discussion_thread_id=None, length=None,
        is_returnable=None, amount=None, has_options=None, width=None,
        image_pairs=None, base_price=None, list_discount_prc=None,
        list_discount=None, **kwargs
    ):

        self.list_price = list_price
        self.weight = weight
        self.out_of_stock_actions = out_of_stock_actions
        self.is_oper = is_oper
        self.age_verification = age_verification
        self.height = height
        self.is_pbp = is_pbp
        self.unlimited_download = unlimited_download
        self.exceptions_type = exceptions_type
        self.is_op = is_op
        self.updated_timestamp = updated_timestamp
        self.free_shipping = free_shipping
        self.product_code = product_code
        self.avail_since = avail_since
        self.main_category = main_category
        self.discussion_type = discussion_type
        self.shipping_freight = shipping_freight
        self.company_id = company_id
        self.edp_shipping = edp_shipping
        self.category_ids = category_ids
        self.discounts = discounts
        self.low_avail_limit = low_avail_limit
        self.details_layout = details_layout
        self.age_limit = age_limit
        self.tax_ids = tax_ids
        self.status = status
        self.product = product
        self.shipping_params = shipping_params
        self.timestamp = timestamp
        self.price = price
        self.options_type = options_type
        self.max_qty = max_qty
        self.min_qty = min_qty
        self.return_period = return_period
        self.zero_price_action = zero_price_action
        self.qty_step = qty_step
        self.tracking = tracking
        self.product_type = product_type
        self.product_id = product_id
        self.list_qty_count = list_qty_count
        self.usergroup_ids = usergroup_ids
        self.is_edp = is_edp
        self.discussion_thread_id = discussion_thread_id
        self.length = length
        self.is_returnable = is_returnable
        self.amount = amount
        self.has_options = has_options
        self.width = width
        self.base_price = base_price
        self.list_discount_prc = list_discount_prc
        self.list_discount = list_discount

        self.product_features = [f if isinstance(
                f, CSCartProductFeature
            ) else CSCartProductFeature().from_json(f)
            for f in product_features.values()
        ] if product_features else []

        self.product_options = [f if isinstance(
                f, CSCartProductOption
            ) else CSCartProductOption().from_json(f)
            for f in product_options.values()
        ] if product_options else []

        self.product_combinations = [f if isinstance(
                f, CSCartProductOptionCombination
            ) else CSCartProductOptionCombination().from_json(f)
            for f in product_combinations
        ] if product_combinations else []

        self.image_pairs = [i if isinstance(
                i, CSCartProductImagePair
            ) else CSCartProductImagePair().from_json(i)
            for i in image_pairs.values()
        ] if image_pairs else []

        self.main_pair = main_pair \
            if isinstance(
                main_pair, CSCartProductMainPair
            ) else CSCartProductMainPair().from_json(main_pair)

        for k, v in kwargs.items():
            setattr(self, k, v)


class CSCartProductFeatureVariant(CSCartResource):

    def __init__(
        self, value_int=None, variant=None, value=None, variant_id=None,
        image_pairs=None, **kwargs
    ):

        self.value_int = value_int
        self.variant = variant
        self.value = value
        self.variant_id = variant_id

        self.image_pairs = image_pairs \
            if isinstance(
                image_pairs, CSCartProductImagePair
            ) or not image_pairs \
            else CSCartProductImagePair().from_json(image_pairs)

        for k, v in kwargs.items():
            setattr(self, k, v)


class CSCartProductFeature(CSCartResource):

    def __init__(
        self, description=None, variant=None, value=None, feature_id=None,
        parent_id=None, prefix=None, suffix=None, features_hash=None,
        variant_id=None, value_int=None, variants=None, feature_type=None,
        **kwargs
    ):

        self.description = description
        self.variant = variant
        self.value = value
        self.feature_id = feature_id
        self.parent_id = parent_id
        self.prefix = prefix
        self.suffix = suffix
        self.features_hash = features_hash
        self.variant_id = variant_id
        self.value_int = value_int
        self.feature_type = feature_type

        self.variants = [v if isinstance(
                v, CSCartProductFeatureVariant
            ) else CSCartProductFeatureVariant().from_json(v)
            for v in variants.values()
        ] if variants else []

        for k, v in kwargs.items():
            setattr(self, k, v)


class CSCartProductOption(CSCartResource):

    def __init__(
        self, option_id=None, product_id=None, company_id=None,
        option_type=None, inventory=None, regexp=None, required=None,
        multiupload=None, allowed_extensions=None, max_file_size=None,
        missing_variants_handling=None, status=None, position=None, value=None,
        option_name=None, option_text=None, description=None, inner_hint=None,
        incorrect_message=None, comment=None, variants=None, **kwargs
    ):

        self.option_id = option_id
        self.product_id = product_id
        self.company_id = company_id
        self.option_type = option_type
        self.inventory = inventory
        self.regexp = regexp
        self.required = required
        self.multiupload = multiupload
        self.allowed_extensions = allowed_extensions
        self.max_file_size = max_file_size
        self.missing_variants_handling = missing_variants_handling
        self.status = status
        self.position = position
        self.value = value
        self.option_name = option_name
        self.option_text = option_text
        self.description = description
        self.inner_hint = inner_hint
        self.incorrect_message = incorrect_message
        self.comment = comment

        self.variants = [v if isinstance(
                v, CSCartProductFeatureVariant
            ) else CSCartProductFeatureVariant().from_json(v)
            for v in variants.values()
        ] if variants else []

        for k, v in kwargs.items():
            setattr(self, k, v)


class CSCartProductOptionCombination(CSCartResource):

    def __init__(
        self, product_id=None, product_code=None, combination_hash=None,
        combination=None, amount=None, temp=None, position=None,
        image_pairs=None, **kwargs
    ):

        self.product_id = product_id
        self.product_code = product_code
        self.combination_hash = combination_hash
        self.combination = combination
        self.amount = amount
        self.temp = temp

        self.position = position
        self.image_pairs = [i if isinstance(
                i, CSCartProductImagePair
            ) else CSCartProductImagePair().from_json(i)
            for i in (image_pairs.values() if isinstance(image_pairs, list) else [image_pairs])
        ] if image_pairs else []

        for k, v in kwargs.items():
            setattr(self, k, v)


class CSCartProductException(CSCartResource):

    def __init__(
        self, exception_id=None, product_id=None, combination=None, **kwargs
    ):

        self.exception_id = exception_id
        self.product_id = product_id
        self.combination = combination

        for k, v in kwargs.items():
            setattr(self, k, v)
