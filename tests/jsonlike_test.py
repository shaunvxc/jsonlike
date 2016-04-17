# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sure
import json

from jsonlike import unwrap_and_load, loads

def test_loads_w_bad_double_quotes():
    loads('{"a":1, "b": 2, "c":""shaun""}').should.equal(json.loads('{"a":1, "b": 2, "c": "shaun"}'))


def test_unwrap_and_loads():
    unwrap_and_load('json13123({"a":1, "b": 2, "c":""shaun""})').should.equal(json.loads('{"a":1, "b": 2, "c": "shaun"}'))


def test_loads_w_html():
    loads('{"a":1, "b": 2, "c": "<font class="stupid_font" balh/>hey"}').should.equal(json.loads('{"a":1, "b": 2, "c": "hey"}'))


def test_loads_w_html2():
    loads('{"a":1, "b": 2, "c": "<font class="stupid_font">hey</font>"}').should.equal(json.loads('{"a":1, "b": 2, "c": "hey"}'))
