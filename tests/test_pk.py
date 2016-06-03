#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import os
from os.path import join
from datetime import datetime
from dataIO import py23
from dataIO import pk
from dataIO import textfile

path_pk = os.path.abspath("test.pickle")
path_gz = os.path.abspath("test.pickle.gz")

data = {
    "int": 100,
    "float": 3.1415926535,
    "str": "string 字符串",
    "bytes": "bytes 比特串".encode("utf-8"),
    "boolean": True,
    "datetime": datetime.now(),
}


def test_is_pickle_file():
    assert pk.is_pickle_file("test.pickle") is True
    assert pk.is_pickle_file("test.PICKLE") is True
    assert pk.is_pickle_file("test.pk") is True
    assert pk.is_pickle_file("test.PK") is True
    assert pk.is_pickle_file("test.p") is True
    assert pk.is_pickle_file("test.P") is True
    assert pk.is_pickle_file("test.pickle.tmp") is True
    assert pk.is_pickle_file("test.pk.tmp") is True
    assert pk.is_pickle_file("test.p.tmp") is True

    assert pk.is_pickle_file("test.gz") is False
    assert pk.is_pickle_file("test.GZ") is False
    assert pk.is_pickle_file("test.gz.tmp") is False

    with pytest.raises(pk.PickleExtError) as exc_info:
        pk.is_pickle_file("test.txt")


def test_prevent_overwrite(tmpdir):
    """Test whether file overwrite alert is working.
    """
    textfile.write("hello", path_pk)
    pk.dump([1, 2, 3], path_pk)
    os.remove(path_pk)


def test_compress():
    """Test whether data compression is working.
    """
    pk.safe_dump({"value": 1}, path_gz, enable_verbose=False)
    assert pk.load(path_gz, enable_verbose=False) == {"value": 1}
    os.remove(path_gz)


def test_obj2_bytes_or_str():
    assert data == pk.str2obj(pk.obj2str(data))
    assert data == pk.bytes2obj(pk.obj2bytes(data))

if __name__ == "__main__":
    import py
    import os
    py.test.cmdline.main("%s --tb=native -s" % os.path.basename(__file__))
