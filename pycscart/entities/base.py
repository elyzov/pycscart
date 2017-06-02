import json
from pycscart.utils import CSCartJsonEncoder, CSCartMinimalJsonEncoder


class CSCartObject(object):

    """Base CS-Cart object."""

    def __repr__(self):
        return "{cls}::{obj}".format(cls=self.__class__.__name__, obj=self.to_json())

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def json_repr(self, minimal=False):
        """Construct a JSON-friendly representation of the object.

        :param bool minimal: Construct a minimal representation of the object (ignore nulls and empty collections)

        :rtype: dict
        """
        data = {}

        if minimal:
            for k, v in vars(self).items():
                if (v or v is False or v == 0):
                    data.update(dict({k: v}))
        else:
            for k, v in vars(self).items():
                data.update(dict({k: v}))

        return data

    @classmethod
    def from_json(cls, attributes):
        """Construct an object from a parsed response.

        :param dict attributes: object attributes from parsed response
        """
        attrs = {}
        if attributes:
	        for k, v in attributes.items():
	            attrs.update(dict({k: v}))

        return cls(**attrs)

    def to_json(self, minimal=True):
        """Encode an object as a JSON string.

        :param bool minimal: Construct a minimal representation of the object (ignore nulls and empty collections)

        :rtype: str
        """
        if minimal:
            return json.dumps(self.json_repr(minimal=True), cls=CSCartMinimalJsonEncoder, indent=4, sort_keys=False)
        else:
            return json.dumps(self.json_repr(), cls=CSCartJsonEncoder, indent=4, sort_keys=False)


class CSCartResource(CSCartObject):

    """Base CSCart resource."""

    def __repr__(self):
        return "{cls}::{obj}".format(cls=self.__class__.__name__, obj=self.to_json())

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return "{cls}::".format(cls=self.__class__.__name__) + str(self.__dict__)
