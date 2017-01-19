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


def loads(content, try_yaml=False):
    try:
        json.loads(content)
    except Exception:
        cleaned = clean_json(content)
        try:
            # strip out HTML content and unescaped chars
            return json.loads(cleaned)
        except Exception:
            # try using demjson to decode a non-strict json string
            try:
                return demjson.decode(cleaned)
            except Exception:
                if try_yaml:
                    # try loading as yaml-- yaml is a superset of json..this could be dangerous in cases
                    return yaml.load(cleaned)
                raise

def clean_json(content):
    return remove_html(remove_bad_double_quotes(remove_invalid_escapes(add_missing_commas(content))))


def process_repl(match):
    return match.group(2)


def remove_bad_blocks(block_pairs, content):
    x = content
    for pair in block_pairs:
        x = remove_bad_block(pair[0], pair[1], x)

    return x


def remove_bad_block(key_name_to_rem, key_to_stop_rem_at, content):
    if '"{}"'.format(key_name_to_rem) in content:
        x = re.sub('(\"{}\":.{{1,}})(\"{}\")'.format(key_name_to_rem, key_to_stop_rem_at), process_repl, content, flags=re.DOTALL)
        return x

    return content


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
