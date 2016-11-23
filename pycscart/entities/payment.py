from .base import CSCartResource


class CSCartPayment(CSCartResource):

    def __init__(
        self, payment=None, a_surcharge=None, company_id=None, description=None,
        image=None, instructions=None, lang_code=None, localization=None,
        p_surcharge=None, payment_category=None, payment_id=None, position=None,
        processor=None, processor_id=None, processor_params=None,
        processor_type=None, status=None, surcharge_title=None, tax_ids=None,
        template=None, usergroup_ids=None
    ):

        self.payment = payment
        self.a_surcharge = a_surcharge
        self.company_id = company_id
        self.description = description
        self.image = image
        self.instructions = instructions
        self.lang_code = lang_code
        self.localization = localization
        self.p_surcharge = p_surcharge
        self.payment_category = payment_category
        self.payment_id = payment_id
        self.position = position
        self.processor = processor
        self.processor_id = processor_id
        self.processor_params = processor_params
        self.processor_type = processor_type
        self.status = status
        self.surcharge_title = surcharge_title
        self.tax_ids = tax_ids
        self.template = template
        self.usergroup_ids = usergroup_ids
