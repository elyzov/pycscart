from .base import CSCartResource


class CSCartOrder(CSCartResource):

    def __init__(
        self, api_key=None, b_address=None, b_address_2=None, b_city=None,
        b_country=None, b_country_descr=None, b_county=None, b_firstname=None,
        b_lastname=None, b_phone=None, b_state=None, b_state_descr=None,
        b_zipcode=None, birthday=None, company=None, company_id=None,
        credit_memo_id=None, details=None, discount=None,
        display_shipping_cost=None, display_subtotal=None, doc_ids=None,
        email=None, fax=None, fields=None, firstname=None, invoice_id=None,
        ip_address=None, is_parent_order=None, is_root=None, issuer_id=None,
        janrain_identifier=None, lang_code=None, last_passwords=None,
        lastname=None, localization_id=None, need_shipping=None, notes=None,
        order_id=None, parent_order_id=None, password_change_timestamp=None,
        payment_id=None, payment_info=None, payment_method=None,
        payment_surcharge=None, phone=None, points=None, points_info=None,
        product_groups=None, products=None, profile_id=None, promotion_ids=None,
        promotions=None, purchase_timestamp_from=None,
        purchase_timestamp_to=None, repaid=None, responsible_email=None,
        s_address=None, s_address_2=None, s_address_type=None, s_city=None,
        s_country_descr=None, s_county=None, s_firstname=None, s_lastname=None,
        s_phone=None, s_state=None, s_state_descr=None, s_zipcode=None,
        secondary_currency=None, shipment_ids=None, shipping=None,
        shipping_cost=None, shipping_ids=None, status=None, subtotal=None,
        subtotal_discount=None, tax_exempt=None, tax_subtotal=None, taxes=None,
        timestamp=None, total=None, url=None, user_id=None,
        validation_code=None, **kwargs
    ):

        self.api_key = api_key
        self.b_address = b_address
        self.b_address_2 = b_address_2
        self.b_city = b_city
        self.b_country = b_country
        self.b_country_descr = b_country_descr
        self.b_county = b_county
        self.b_firstname = b_firstname
        self.b_lastname = b_lastname
        self.b_phone = b_phone
        self.b_state = b_state
        self.b_state_descr = b_state_descr
        self.b_zipcode = b_zipcode
        self.birthday = birthday
        self.company = company
        self.company_id = company_id
        self.credit_memo_id = credit_memo_id
        self.details = details
        self.discount = discount
        self.display_shipping_cost = display_shipping_cost
        self.display_subtotal = display_subtotal
        self.doc_ids = doc_ids
        self.email = email
        self.fax = fax
        self.fields = fields
        self.firstname = firstname
        self.invoice_id = invoice_id
        self.ip_address = ip_address
        self.is_parent_order = is_parent_order
        self.is_root = is_root
        self.issuer_id = issuer_id
        self.janrain_identifier = janrain_identifier
        self.lang_code = lang_code
        self.last_passwords = last_passwords
        self.lastname = lastname
        self.localization_id = localization_id
        self.need_shipping = need_shipping
        self.notes = notes
        self.order_id = order_id
        self.parent_order_id = parent_order_id
        self.password_change_timestamp = password_change_timestamp
        self.payment_id = payment_id
        self.payment_info = payment_info
        self.payment_method = payment_method
        self.payment_surcharge = payment_surcharge
        self.phone = phone
        self.points = points
        self.points_info = points_info
        self.product_groups = product_groups
        self.products = products
        self.profile_id = profile_id
        self.promotion_ids = promotion_ids
        self.promotions = promotions
        self.purchase_timestamp_from = purchase_timestamp_from
        self.purchase_timestamp_to = purchase_timestamp_to
        self.repaid = repaid
        self.responsible_email = responsible_email
        self.s_address = s_address
        self.s_address_2 = s_address_2
        self.s_address_type = s_address_type
        self.s_city = s_city
        self.s_country_descr = s_country_descr
        self.s_county = s_county
        self.s_firstname = s_firstname
        self.s_lastname = s_lastname
        self.s_phone = s_phone
        self.s_state = s_state
        self.s_state_descr = s_state_descr
        self.s_zipcode = s_zipcode
        self.secondary_currency = secondary_currency
        self.shipment_ids = shipment_ids
        self.shipping = shipping
        self.shipping_cost = shipping_cost
        self.shipping_ids = shipping_ids
        self.status = status
        self.subtotal = subtotal
        self.subtotal_discount = subtotal_discount
        self.tax_exempt = tax_exempt
        self.tax_subtotal = tax_subtotal
        self.taxes = taxes
        self.timestamp = timestamp
        self.total = total
        self.url = url
        self.user_id = user_id
        self.validation_code = validation_code

        for k, v in kwargs.items():
            setattr(self, k, v)
