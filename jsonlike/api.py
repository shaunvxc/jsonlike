# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import demjson
import yaml
import re
import unwrapper


def unwrap_and_load(content):
    cleaned = clean_json(unwrapper.unwrap_raw(content))
    return loads(cleaned)


def loads(content):
    cleaned = clean_json(content)
    try:
        # strip out HTML content and unescaped chars
        return json.loads(cleaned)
    except Exception:
        try:
            # try loading it as YAML
            return yaml.load(cleaned)
        except Exception:
            # try using demjson to decode a non-strict json string
            return demjson.decode(cleaned)


def clean_json(content):
    return remove_html(remove_bad_double_quotes(remove_invalid_escapes(add_missing_commas(content))))


def sub_first(match):
    return match.group(1) + '"'


def sub_last(match):
    return '"' + match.group(1)


def remove_bad_double_quotes(content):
    # JSON requires values to be surrounded in " 's, ie `{"foo": "bar"}`. This handles
    # cases where the JSON is like `{"foo":""bar""}`--- json.loads() won't like this case !
    return re.sub('([^\:])\"\"', sub_first, re.sub(r'\"\"([^,])', sub_last, content))


def remove_html(content):
    return re.sub('<[^<]+?>', '', content)


def remove_invalid_escapes(content):
    return content.replace("\\", "")


def add_missing_commas(content):
    return content.replace('"}', '",}')
