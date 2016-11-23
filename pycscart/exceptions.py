class CSCartError(Exception):
    pass


class CSCartUnsupportedVersion(CSCartError):

    def __init__(self, curver, reqver, method):
        self.curver = curver
        self.reqver = reqver
        self.method = method

        super(CSCartError, self).__init__(self.__str__())

    def __repr__(self):
        return 'CSCartUnsupportedVersion: version "{curver}" is not supported with method "{method}" (required "{reqver}").' \
            .format(
                curver=self.curver, reqver=self.reqver, method=self.method
            )

    def __str__(self):
        return self.__repr__()


class CSCartUnsupportedBrand(CSCartError):

    def __init__(self, brand, method):
        self.brand = brand
        self.method = method

        super(CSCartError, self).__init__(self.__str__())

    def __repr__(self):
        return 'CSCartUnsupportedBrand: "{brand}" brand could not use method "{method}"' \
            .format(brand=self.brand, method=self.method)

    def __str__(self):
        return self.__repr__()


class CSCartHttpError(CSCartError):

    def __init__(self, response):
        self.error_message = response.reason or ''
        if response.content:
            content = response.json()
            self.error_message = content.get('message', self.error_message)
        self.status_code = response.status_code
        super(CSCartHttpError, self).__init__(self.__str__())

    def __repr__(self):
        return 'CSCartHttpError: HTTP %s returned with message, "%s"' % \
               (self.status_code, self.error_message)

    def __str__(self):
        return self.__repr__()


class BadRequestError(CSCartHttpError):
    pass


class UnauthorizedError(CSCartHttpError):
    pass


class ForbiddenError(CSCartHttpError):
    pass


class NotFoundError(CSCartHttpError):
    pass


class MethodNotAllowedError(CSCartHttpError):
    pass


class NotAcceptableError(CSCartHttpError):
    pass


class UnsupportedMediaTypeError(CSCartHttpError):
    pass


class InternalServerError(CSCartHttpError):
    pass
