import collections
import datetime
import sys

try:
    import json
except ImportError:
    import simplejson as json


def is_stringy(obj):
    is_python3 = sys.version_info[0] == 3
    if is_python3:
        string_types = str,
    else:
        string_types = basestring,
    return isinstance(obj, string_types)


class CSCartJsonEncoder(json.JSONEncoder):

    """Custom JSON encoder for CS-Cart object serialization."""

    def default(self, obj):
        if hasattr(obj, 'json_repr'):
            return self.default(obj.json_repr())

        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

        if isinstance(obj, collections.Iterable) and not is_stringy(obj):
            try:
                return {k: self.default(v) for k, v in obj.items()}
            except AttributeError:
                return [self.default(e) for e in obj]

        return obj


class CSCartMinimalJsonEncoder(json.JSONEncoder):

    """Custom JSON encoder for CS-Cart object serialization."""

    def default(self, obj):
        if hasattr(obj, 'json_repr'):
            return self.default(obj.json_repr(minimal=True))

        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

        if isinstance(obj, collections.Iterable) and not is_stringy(obj):
            try:
                return {k: self.default(v) for k, v in obj.items() if (v or v in (False, 0))}
            except AttributeError:
                return [self.default(e) for e in obj if (e or e in (False, 0))]

        return obj
