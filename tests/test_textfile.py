#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from dataIO import textfile


path = os.path.abspath(__file__)

with open(path, "rb") as f:
    f_lines = [line.decode("utf-8") for line in f]


def test_readlines():
    result = list(textfile.readlines(path, strip=None))
    assert result == f_lines

    result = list(textfile.readlines(path, skiplines=3, strip=None))
    assert result == f_lines[3:]

    result = list(textfile.readlines(path, nlines=3, strip=None))
    assert result == f_lines[:3]

    result = list(textfile.readlines(path, skiplines=3, nlines=3, strip=None))
    assert result == f_lines[3:3 + 3]


def test_readchunks():
    result = list(textfile.readchunks(path, strip=None))
    assert result[0] == f_lines[0:1]

    result = list(textfile.readchunks(path, skiplines=3, strip=None))
    assert result[0] == f_lines[3:4]

    result = list(textfile.readchunks(path, chunksize=3, strip=None))
    assert result[0] == f_lines[0:3]

    result = list(textfile.readchunks(
        path, skiplines=3, chunksize=3, strip=None))
    assert result[0] == f_lines[3:6]

if __name__ == "__main__":
    import py
    import os
    py.test.cmdline.main("%s --tb=native -s" % os.path.basename(__file__))
