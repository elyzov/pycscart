#!/usr/bin/env python

import re
import requests
import requests.exceptions
import requests.status_codes
import pycscart

from packaging.version import Version

from .entities import CSCartSetting, CSCartBlock, \
                      CSCartCart, CSCartCallRequest, CSCartCategory, \
                      CSCartLanguage, CSCartLangvar, CSCartOrder, CSCartPage, \
                      CSCartVendor, CSCartDiscussion, CSCartPayment, \
                      CSCartProduct, CSCartProductFeature, \
                      CSCartProductOption, CSCartProductOptionCombination, \
                      CSCartProductException, CSCartShipment, CSCartShipping, \
                      CSCartStatus, CSCartStore, CSCartTax, CSCartUser, \
                      CSCartUsergroup

from .exceptions import CSCartUnsupportedVersion, CSCartUnsupportedBrand, \
                        CSCartError, CSCartHttpError, BadRequestError, \
                        UnauthorizedError, ForbiddenError, NotFoundError, \
                        MethodNotAllowedError, NotAcceptableError, \
                        UnsupportedMediaTypeError, InternalServerError


class CSCartClient(object):

    """Client interface for the CS-Cart REST API."""

    CSCART_API_MIN_VERSION = '4.0.0'

    def __init__(
        self, url, username=None, api_key=None, brand=None, version=None,
        edition=None, timeout=10, session=None
    ):
        if session is None:
            self.session = requests.Session()
        else:
            self.session = session

        self.api_url = ''.join([url.rstrip('/'), '/api'])
        self.auth = (username, api_key) if username and api_key else None
        self.timeout = timeout

        if brand and version:
            self.brand, self.version, self.edition = brand, version, edition
        else:
            info = self.get_info()
            self.brand, self.version, self.edition = \
                info['brand'], info['version'], info['edition']

    def __repr__(self):
        return 'Connection: %s' % self.api_url

    def _do_request(self, method, path, params=None, data=None):
        headers = {
            'Content-Type': 'application/json', 'Accept': 'application/json'}

        url = ''.join([self.api_url.rstrip('/'), path])

        try:
            response = self.session.request(
                method, url, params=params, data=data, headers=headers,
                auth=self.auth, timeout=self.timeout
                )
            pycscart.log.info('Got response from %s', url)
        except requests.exceptions.RequestException as e:
            pycscart.log.error(
                'Error while getting response from %s: %s', url, str(e)
            )

        if response is None:
            raise CSCartError("Couldn't connect to CS-Cart API endpoint")

        if response.status_code >= 500:
            pycscart.log.error('Got HTTP {code}: {body}'.format(
                code=response.status_code, body=response.text))
            raise InternalServerError(response)
        elif response.status_code >= 400:
            pycscart.log.error('Got HTTP {code}: {body}'.format(
                code=response.status_code, body=response.text))
            if response.status_code == requests.codes.bad_request:
                raise BadRequestError(response)
            elif response.status_code == requests.codes.unauthorized:
                raise UnauthorizedError(response)
            elif response.status_code == requests.codes.forbidden:
                raise ForbiddenError(response)
            elif response.status_code == requests.codes.not_found:
                raise NotFoundError(response)
            elif response.status_code == requests.codes.method_not_allowed:
                raise MethodNotAllowedError(response)
            elif response.status_code == requests.codes.not_acceptable:
                raise NotAcceptableError(response)
            elif response.status_code == requests.codes.unsupported_media_type:
                raise UnsupportedMediaTypeError(response)
            else:
                pycscart.log.error('Got HTTP {code}: {body}'.format(
                    code=response.status_code, body=response.text))
                raise CSCartHttpError(response)
        elif response.status_code >= 300:
            pycscart.log.warn('Got HTTP {code}: {body}'.format(
                code=response.status_code, body=response.text))
        else:
            pycscart.log.debug('Got HTTP {code}: {body}'.format(
                code=response.status_code, body=response.text))

        return response

    @staticmethod
    def _parse_response(response, cls, is_list=False, is_dict=False, resource_name=None):
        target = response.json()[
            resource_name] if resource_name else response.json()
        if is_list:
            return [cls.from_json(resource) for resource in target]
        elif is_dict:
            return [cls.from_json(resource) for resource in target.values()]
        else:
            return cls.from_json(target)

    @staticmethod
    def _parse_info(text):
        fields, data = ['brand', 'version', 'edition'], re.sub('<[^<]+?>', '', text)
        return dict(zip(fields, filter(None, data.split(' '))))

    def hello(self):
        return "Hello"

    def get_info(self):
        params = {
            'version': True
        }

        response = self._do_request('GET', '/', params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_info(response.text)
            data = {
                'brand': data.get('brand', None),
                'version': Version(data.get('version', CSCartClient.CSCART_API_MIN_VERSION)),
                'edition': data.get('edition', None)
            }
        else:
            data = {}

        return data

    def is_cscart(self):
        return self.is_brand('CS-Cart')

    def is_multivendor(self):
        return self.is_brand('Multi-Vendor')

    def is_brand(self, brand):
        return self.brand.lower() == brand.lower()

    def min_supported_version(ver=None):
        def decorator(method):
            def wrapper(self, *args, **kwargs):
                required_ver = Version(ver) if ver else Version(self.CSCART_API_MIN_VERSION)
                if self.version < required_ver:
                    raise CSCartUnsupportedVersion(self.version, required_ver, method.__name__)
                else:
                    return method(self, *args, **kwargs)
            return wrapper
        return decorator

    def supported_brand(brand):
        def decorator(method):
            def wrapper(self, *args, **kwargs):
                if self.is_brand(brand):
                    return method(self, *args, **kwargs)
                else:
                    raise CSCartUnsupportedBrand(self.brand, method.__name__)
            return wrapper
        return decorator

    def list_orders(
        self, page=None, items_per_page=10, sort_by='date',
        sort_order='desc', status=None, user_id=None, company_id=None,
        email=None, invoice_id=None, credit_memo_id=None, time_from=None,
        time_to=None, period=None
    ):
        params = {
            'page': page,
            'items_per_page': items_per_page,
            'sort_by': sort_by,
            'sort_order': sort_order,
            'status': status,
            'user_id': user_id,
            'company_id': company_id,
            'email': email,
            'invoice_id': invoice_id,
            'credit_memo_id': credit_memo_id,
            'period': period,
            'time_from': time_from,
            'time_to': time_to
        }

        response = self._do_request('GET', '/orders', params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartOrder, is_list=True, resource_name='orders')
        else:
            data = False

        return data

    def get_order(self, order_id):
        response = self._do_request('GET', '/orders/%s' % order_id)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartOrder)
        else:
            data = False

        return data

    def delete_order(self, order_id=None):
        response = self._do_request('DELETE', '/orders/%s' % order_id)

        return response.status_code == requests.codes.no_content

    def list_settings(self, items_per_page=10, page=None):
        params = {
            'page': page,
            'items_per_page': items_per_page
        }

        response = self._do_request('GET', '/settings', params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartSetting, is_list=True, resource_name='settings')
        else:
            data = False

        return data

    def get_setting(self, object_id):
        response = self._do_request('GET', '/settings/%s' % object_id)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartSetting)
        else:
            data = False

        return data

    def list_blocks(self):
        response = self._do_request('GET', '/blocks')

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartBlock, is_list=True)
        else:
            data = False

        return data

    def get_block(self, block_id):
        response = self._do_request('GET', '/blocks/%s' % block_id)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartBlock)
        else:
            data = False

        return data

    def delete_block(self, block_id=None):
        response = self._do_request('DELETE', '/blocks/%s' % block_id)

        return response.status_code == requests.codes.no_content

    @min_supported_version("4.3.5")
    def list_carts(
        self, page=1, items_per_page=10, sort_by='name',
        sort_order='desc', cname=None, email=None, user_id=None,
        with_info_only=False, users_type=None, total_from=None, total_to=None,
        product_type_c=False, product_type_w=False, period=None,
        time_from=None, time_to=None, p_ids=None
    ):
        params = {
            'page': page,
            'items_per_page': items_per_page,
            'sort_by': sort_by,
            'sort_order': sort_order,
            'cname': cname,
            'email': email,
            'user_id': user_id,
            'with_info_only': with_info_only,
            'users_type': users_type,
            'total_from': total_from,
            'total_to': total_to,
            'product_type_c': product_type_c,
            'product_type_w': product_type_w,
            'period': period,
            'time_from': time_from,
            'time_to': time_to,
            'p_ids': p_ids
        }

        response = self._do_request('GET', '/carts', params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartCart, is_list=True, resource_name='carts')
        else:
            data = False

        return data

    @min_supported_version("4.3.5")
    def get_cart(self, user_id):
        response = self._do_request('GET', '/carts/%s' % user_id)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartCart)
        else:
            data = False

        return data

    def delete_cart(self, cart_id=None):
        response = self._do_request('DELETE', '/carts/%s' % cart_id)

        return response.status_code == requests.codes.no_content

    @min_supported_version("4.3.5")
    def list_callrequests(
        self, page=1, items_per_page=10, sort_by='date',
        sort_order='desc', status=None, name=None, phone=None, company_id=None,
        order_status=None, user_id=None, order_exists=None
    ):
        params = {
            'page': page,
            'items_per_page': items_per_page,
            'sort_by': sort_by,
            'sort_order': sort_order,
            'status': status,
            'name': name,
            'phone': phone,
            'company_id': company_id,
            'order_status': order_status,
            'user_id': user_id,
            'order_exists': order_exists
        }

        response = self._do_request('GET', '/call_requests', params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartCallRequest, is_list=True, resource_name='call_requests')
        else:
            data = False

        return data

    @min_supported_version("4.3.5")
    def get_callrequest(self, request_id):
        response = self._do_request('GET', '/call_requests/%s' % request_id)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartCallRequest)
        else:
            data = False

        return data

    @min_supported_version("4.3.5")
    def delete_callrequest(self, callrequest_id=None):
        response = self._do_request('DELETE', '/call_requests/%s' % callrequest_id)

        return response.status_code == requests.codes.no_content

    def list_categories(self, page=1, items_per_page=10):
        params = {
            'page': page,
            'items_per_page': items_per_page
        }

        response = self._do_request('GET', '/categories', params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartCategory, is_list=True, resource_name='categories')
        else:
            data = False

        return data

    def get_category(self, category_id):
        response = self._do_request('GET', '/categories/%s' % category_id)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartCategory)
        else:
            data = False

        return data

    def delete_category(self, category_id=None):
        response = self._do_request('DELETE', '/categories/%s' % category_id)

        return response.status_code == requests.codes.no_content

    @min_supported_version("4.3.5")
    def list_discussions(
        self, page=1, items_per_page=10, sort_by='timestamp',
        sort_order=None, status=None, name=None, message=None, type=None,
        ip_address=None, rating_value=None, object_type=None, object_id=None,
        period=None, time_from=None, time_to=None, product_id=None
    ):
        params = {
            'page': page,
            'items_per_page': items_per_page,
            'sort_by': sort_by,
            'sort_order': sort_order,
            'status': status,
            'name': name,
            'message': message,
            'type': type,
            'ip_address': ip_address,
            'rating_value': rating_value,
            'object_type': object_type,
            'object_id': object_id,
            'period': period,
            'time_from': time_from,
            'time_to': time_to
        }

        url = '/products/%s/discussions' % product_id if product_id else '/discussions'

        response = self._do_request('GET', url, params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartDiscussion, is_list=True, resource_name='discussions')
        else:
            data = False

        return data

    @min_supported_version("4.3.5")
    def get_discussion(self, discussion_id=None, product_id=None):
        url = '/products/%s/discussions/%s' % (product_id, discussion_id) \
            if product_id else '/discussions/%s' % discussion_id

        response = self._do_request('GET', url)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartDiscussion)
        else:
            data = False

        return data

    @min_supported_version("4.3.5")
    def delete_discussion(self, discussion_id=None, product_id=None):
        url = '/products/%s/discussions/%s' % (product_id, discussion_id) \
            if product_id else '/discussions/%s' % discussion_id

        response = self._do_request('DELETE', url)

        return response.status_code == requests.codes.no_content

    def list_languages(self, page=1, items_per_page=10):
        params = {
            'page': page,
            'items_per_page': items_per_page
        }

        response = self._do_request('GET', '/languages', params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(
                response, CSCartLanguage, is_dict=True,
                resource_name='languages'
            )
        else:
            data = False

        return data

    def get_language(self, lang_id=None):
        response = self._do_request('GET', '/languages/%s' % lang_id)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartLanguage)
        else:
            data = False

        return data

    def delete_language(self, lang_id=None):
        response = self._do_request('DELETE', '/languages/%s' % lang_id)

        return response.status_code == requests.codes.no_content

    def list_langvars(self, page=1, items_per_page=10):
        params = {
            'page': page,
            'items_per_page': items_per_page
        }

        response = self._do_request('GET', '/langvars', params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartLangvar, is_list=True, resource_name='langvars')
        else:
            data = False

        return data

    def get_langvar(self, name='', lang_code='en'):
        params = {
            'sl': lang_code
        }

        response = self._do_request('GET', '/langvars/%s' % name, params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartLangvar)
        else:
            data = False

        return data

    def delete_langvar(self, name=None):
        response = self._do_request('DELETE', '/langvars/%s' % name)

        return response.status_code == requests.codes.no_content

    @min_supported_version("4.3.5")
    def list_pages(
        self, page=1, items_per_page=10, sort_by='position',
        sort_order='desc', parent_id=None, page_type='T', simple=None,
        query=None, status=None, item_ids=None, get_tree=None
    ):
        params = {
            'page': page,
            'items_per_page': items_per_page,
            'sort_by': sort_by,
            'sort_order': sort_order,
            'parent_id': parent_id,
            'page_type': page_type,
            'simple': simple,
            'q': query,
            'status': status,
            'item_ids': item_ids,
            'get_tree': get_tree
        }

        response = self._do_request('GET', '/pages', params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartPage, is_list=True, resource_name='pages')
        else:
            data = False

        return data

    @min_supported_version("4.3.5")
    def get_page(self, page_id=None):
        response = self._do_request('GET', '/pages/%s' % page_id)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartPage)
        else:
            data = False

        return data

    @min_supported_version("4.3.5")
    def delete_page(self, page_id=None):
        response = self._do_request('DELETE', '/pages/%s' % page_id)

        return response.status_code == requests.codes.no_content

    def list_payments(self, page=1, items_per_page=10):
        params = {
            'page': page,
            'items_per_page': items_per_page
        }

        response = self._do_request('GET', '/payments', params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartPayment, is_list=True, resource_name='payments')
        else:
            data = False

        return data

    def get_payment(self, payment_id=None):
        response = self._do_request('GET', '/payments/%s' % payment_id)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartPayment)
        else:
            data = False

        return data

    def delete_payment(self, payment_id=None):
        response = self._do_request('DELETE', '/payments/%s' % payment_id)

        return response.status_code == requests.codes.no_content

    def list_products(
        self, pname=None, pshort=None, pfull=None, pkeywords=None,
        pcode=None, cid=None, amount_from=None, amount_to=None, price_from=None,
        price_to=None, subcats=None, order_ids=None, free_shipping=None,
        status=None, list_price=None, product=None, price=None, code=None,
        amount=None, page=1, items_per_page=10
    ):
        params = {
            'pname': pname,
            'pshort': pshort,
            'pfull': pfull,
            'pkeywords': pkeywords,
            'pcode': pcode,
            'cid': cid,
            'amount_from': amount_from,
            'amount_to': amount_to,
            'price_from': price_from,
            'price_to': price_to,
            'subcats': subcats,
            'order_ids': order_ids,
            'free_shipping': free_shipping,
            'status': status,
            'list_price': list_price,
            'product': product,
            'price': price,
            'code': code,
            'amount': amount,
            'page': page,
            'items_per_page': items_per_page
        }

        response = self._do_request('GET', '/products', params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartProduct, is_list=True, resource_name='products')
        else:
            data = False

        return data

    def get_product(self, product_id=None):
        response = self._do_request('GET', '/products/%s' % product_id)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartProduct)
        else:
            data = False

        return data

    def delete_product(self, product_id=None, category_id=None):
        url = '/categories/%s/products/%s' % (category_id, product_id) \
            if category_id else '/products/%s' % product_id

        response = self._do_request('DELETE', url)

        return response.status_code == requests.codes.no_content

    def list_product_features(self, page=1, items_per_page=10, product_id=None):
        params = {
            'page': page,
            'items_per_page': items_per_page,
            'product_id': product_id
        }

        response = self._do_request('GET', '/features', params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartProductFeature, is_list=True, resource_name='features')
        else:
            data = False

        return data

    def get_product_feature(self, feature_id=None):
        response = self._do_request('GET', '/features/%s' % feature_id)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartProductFeature)
        else:
            data = False

        return data

    def delete_product_feature(self, feature_id=None, product_id=None):
        url = '/products/%s/features/%s' % (product_id, feature_id) \
            if product_id else '/features/%s' % feature_id

        response = self._do_request('DELETE', url)

        return response.status_code == requests.codes.no_content

    def list_product_options(self, product_id=None):
        params = {
            'product_id': product_id
        }

        response = self._do_request('GET', '/options', params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartProductOption, is_dict=True)
        else:
            data = False

        return data

    def list_product_combinations(self, product_id=None):
        params = {
            'product_id': product_id
        }

        response = self._do_request('GET', '/combinations', params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartProductOptionCombination, is_list=True)
        else:
            data = False

        return data

    def delete_product_combination(
        self, combination_hash=None, product_id=None
    ):
        params = {
            'product_id': product_id
        }

        response = self._do_request(
            'DELETE', '/combinations/%s' % combination_hash, params=params
        )

        return response.status_code == requests.codes.no_content

    def get_product_combination(self, combination_id):
        response = self._do_request('GET', '/combinations/%s' % combination_id)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartProductOptionCombination)
        else:
            data = False

        return data

    def list_product_exceptions(self, product_id=None):
        params = {
            'product_id': product_id
        }

        response = self._do_request('GET', '/exceptions', params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartProductException, is_list=True)
        else:
            data = False

        return data

    def get_product_exception(self, exception_id=None):
        response = self._do_request('GET', '/exceptions/%s' % exception_id)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartProductException)
        else:
            data = False

        return data

    def delete_product_exception(
        self, exception_id=None, product_id=None
    ):
        params = {
            'product_id': product_id
        }

        response = self._do_request(
            'DELETE', '/exceptions/%s' % exception_id, params=params
        )

        return response.status_code == requests.codes.no_content

    def list_shipments(self, page=1, items_per_page=10):
        params = {
            'page': page,
            'items_per_page': items_per_page
        }

        response = self._do_request('GET', '/shipments', params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartShipment, is_list=True, resource_name='shipments')
        else:
            data = False

        return data

    def get_shipment(self, shipment_id=None):
        response = self._do_request('GET', '/shipments/%s' % shipment_id)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartShipment)
        else:
            data = False

        return data

    def delete_shipment(self, shipment_id=None):
        response = self._do_request('DELETE', '/shipments/%s' % shipment_id)

        return response.status_code == requests.codes.no_content

    def list_shippings(self, page=1, items_per_page=10):
        params = {
            'page': page,
            'items_per_page': items_per_page
        }

        response = self._do_request('GET', '/shippings', params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(
                response, CSCartShipping, is_list=True,
                resource_name='shippings'
            )
        else:
            data = False

        return data

    def get_shipping(self, shipping_id=None):
        response = self._do_request('GET', '/shippings/%s' % shipping_id)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartShipping)
        else:
            data = False

        return data

    def delete_shipping(self, shipping_id=None):
        response = self._do_request('DELETE', '/shippings/%s' % shipping_id)

        return response.status_code == requests.codes.no_content

    def list_statuses(self, page=1, items_per_page=10):
        params = {
            'page': page,
            'items_per_page': items_per_page
        }

        response = self._do_request('GET', '/statuses', params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(
                response, CSCartStatus, is_list=True, resource_name='statuses'
            )
        else:
            data = False

        return data

    def get_status(self, status_id=None):
        response = self._do_request('GET', '/statuses/%s' % status_id)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartStatus)
        else:
            data = False

        return data

    def delete_status(self, status_id=None):
        response = self._do_request('DELETE', '/statuses/%s' % status_id)

        return response.status_code == requests.codes.no_content

    @supported_brand("CS-Cart")
    def list_stores(
        self, page=1, items_per_page=10, sort_by='name', sort_order='desc',
        timestamp=None, company=None
    ):
        params = {
            'page': page,
            'items_per_page': items_per_page,
            'sort_by': sort_by,
            'sort_order': sort_order,
            'timestamp': timestamp,
            'company': company
        }

        response = self._do_request('GET', '/stores', params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(
                response, CSCartStore, is_list=True, resource_name='stores'
            )
        else:
            data = False

        return data

    @supported_brand("CS-Cart")
    def get_store(self, store_id=None):
        response = self._do_request('GET', '/stores/%s' % store_id)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartStore)
        else:
            data = False

        return data

    @supported_brand("CS-Cart")
    def delete_store(self, company_id=None):
        response = self._do_request('DELETE', '/stores/%s' % company_id)

        return response.status_code == requests.codes.no_content

    def list_taxes(self, page=1, items_per_page=10):
        params = {
            'page': page,
            'items_per_page': items_per_page
        }

        response = self._do_request('GET', '/taxes', params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartTax, is_list=True, resource_name='taxes')
        else:
            data = False

        return data

    def get_tax(self, tax_id=None):
        response = self._do_request('GET', '/taxes/%s' % tax_id)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartTax)
        else:
            data = False

        return data

    def delete_tax(self, tax_id=None):
        response = self._do_request('DELETE', '/taxes/%s' % tax_id)

        return response.status_code == requests.codes.no_content

    def list_users(self, page=1, items_per_page=10):
        params = {
            'page': page,
            'items_per_page': items_per_page
        }

        response = self._do_request('GET', '/users', params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(
                response, CSCartUser, is_list=True, resource_name='users'
            )
        else:
            data = False

        return data

    def get_user(self, user_id=None):
        response = self._do_request('GET', '/users/%s' % user_id)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartUser)
        else:
            data = False

        return data

    def delete_user(self, user_id=None):
        response = self._do_request('DELETE', '/users/%s' % user_id)

        return response.status_code == requests.codes.no_content

    def list_usergroups(self, type='A', status='A', user_id=None):
        params = {
            'type': type,
            'status': status
        }

        url = '/users/%s/usergroups' % user_id if user_id else '/usergroups'
        response = self._do_request('GET', url, params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(
                response, CSCartUsergroup, is_dict=True
            )
        else:
            data = False

        return data

    def get_usergroup(self, usergroup_id=None):
        response = self._do_request('GET', '/usergroups/%s' % usergroup_id)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartUser)
        else:
            data = False

        return data

    def delete_usergroup(self, usergroup_id=None):
        response = self._do_request('DELETE', '/usergroups/%s' % usergroup_id)

        return response.status_code == requests.codes.no_content

    @supported_brand("Multi-Vendor")
    def list_vendors(
        self, page=None, items_per_page=10, sort_by='name', sort_order='desc',
        email=None, timestamp=None, status=None, company=None
    ):
        params = {
            'page': page,
            'items_per_page': items_per_page,
            'sort_by': sort_by,
            'sort_order': sort_order,
            'email': email,
            'timestamp': timestamp,
            'status': status,
            'company': company
        }

        response = self._do_request('GET', '/vendors', params=params)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(
                response, CSCartVendor, is_list=True, resource_name='vendors'
            )
        else:
            data = False

        return data

    @supported_brand("Multi-Vendor")
    def get_vendor(self, vendor_id):
        response = self._do_request('GET', '/vendors/%s' % vendor_id)

        if response.status_code == requests.codes.ok:
            data = self._parse_response(response, CSCartVendor)
        else:
            data = False

        return data

    @supported_brand("Multi-Vendor")
    def delete_vendor(self, vendor_id=None):
        response = self._do_request('DELETE', '/vendors/%s' % vendor_id)

        return response.status_code == requests.codes.no_content
