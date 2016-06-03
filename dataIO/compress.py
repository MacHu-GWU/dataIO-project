#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
data compress utility module.

abbreviation.

- f = file
- s = str
- b = bytes
- p = path
- r = read
- w = write
"""

import gzip
import zlib
import base64


#--- single file ---
def write_gzip(b, path):
    with gzip.open(path, "wb") as f:
        f.write(b)


def read_gzip(path):
    with gzip.open(path, "rb") as f:
        return f.read()


#--- compress/decompress ---
def compress_str(s):
    """use zip and base64 encoding to compress arbitrary utf-8 string to a 
    shorter utf-8 string. 
    
    1. str -> utf-8 bytes
    2. utf-8 bytes --- zip compress ---> bytes
    3. bytes -> urlsafe_b64encode bytes
    4. urlsafe_b64encode bytes -> str
    """
    return base64.b64encode(zlib.compress(s.encode("utf-8"))).decode("utf-8")


def decompress_str(s):
    """opposite of :func:`compress_str`.
    
    1. str -> utf-8 bytes
    2. utf-8 bytes -> b64 decode bytes
    3. urlsafe_b64decode bytes --- zip decompress ---> bytes
    4. bytes -> str
    """
    return zlib.decompress(base64.b64decode(s)).decode("utf-8")