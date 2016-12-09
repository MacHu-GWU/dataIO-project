# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from pytest import approx
import os
from os.path import join
from datetime import datetime
from dataIO import py23
from dataIO import js
from dataIO import textfile

path_json = os.path.abspath("test.json")
path_gz = os.path.abspath("test.json.gz")

data_simple = {
    "int": 100,
    "float": 3.1415926535,
    "str": u"string 字符串",
    "boolean": True,
}

data_complex = {
    "int": 100,
    "float": 3.1415926535,
    "str": u"string 字符串",
    "bytes": u"bytes 比特串".encode("utf-8"),
    "boolean": True,
    "datetime": datetime.now(),
}


def test_is_json_file():
    assert js.is_json_file("test.json") is True
    assert js.is_json_file("test.JSON") is True
    assert js.is_json_file("test.js") is True
    assert js.is_json_file("test.JS") is True
    assert js.is_json_file("test.json.tmp") is True
    assert js.is_json_file("test.js.tmp") is True

    assert js.is_json_file("test.gz") is False
    assert js.is_json_file("test.GZ") is False
    assert js.is_json_file("test.gz.tmp") is False

    with pytest.raises(js.JsonExtError) as exc_info:
        js.is_json_file("test.txt")


def test_prevent_overwrite(tmpdir):
    """Test whether file overwrite alert is working.
    """
    textfile.write("hello", path_json)
    js.dump([1, 2, 3], path_json)
    os.remove(path_json)


def test_float_precision():
    """Test whether ``float_precision`` keywork is working.
    """
    js.safe_dump({"value": 1.23456789}, path_json, indent_format=False,
                 float_precision=2, enable_verbose=False)
    assert js.load(path_json, enable_verbose=False)["value"] == approx(1.23)
    os.remove(path_json)


def test_compress():
    """Test whether data compression is working.
    """
    js.safe_dump({"value": 1}, path_gz, enable_verbose=False)
    assert js.load(path_gz, enable_verbose=False) == {"value": 1}
    os.remove(path_gz)

try:
    from bson import json_util

    def test_bytes_and_datetime():
        js.safe_dump(data_complex, path_json, enable_verbose=False)
        d = js.load(path_json, enable_verbose=False)

        assert d["int"] == data_complex["int"]
        assert d["float"] == data_complex["float"]
        assert d["str"] == data_complex["str"]
        assert d["boolean"] == data_complex["boolean"]

        if py23.is_py3:
            assert d["bytes"].decode("utf-8") == u"bytes 比特串"

        dt1 = d["datetime"]
        dt2 = data_complex["datetime"]

        assert dt1.date() == dt2.date()
        assert dt1.hour, dt2.hour
        assert dt1.minute, dt2.minute
        assert dt1.second, dt2.second
        assert abs(dt1.microsecond - dt2.microsecond) <= 1000

        os.remove(path_json)
except:
    pass


if __name__ == "__main__":
    import os
    pytest.main([os.path.basename(__file__), "--tb=native", "-s", ])
