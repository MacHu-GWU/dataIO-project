#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from dataIO import compress
from dataIO import textfile


b = textfile.readbytes(__file__)
s = b.decode("utf-8")
path = os.path.abspath("compress.gz")


def test_gzip():
    compress.write_gzip(b, path)
    b1 = compress.read_gzip(path)

    assert b == b1
    os.remove(path)


def test_compress_decompress_str():
    s1 = compress.compress_str(s)  # compressed
    s2 = compress.decompress_str(s1)  # decompressed

    # 压缩前的字符串和压缩后的字符串一致
    assert s == s2

    # 压缩后的字符串比压缩前的字符串长度要小
    assert len(s1) <= len(s)

if __name__ == "__main__":
    import py
    import os
    py.test.cmdline.main("%s --tb=native -s" % os.path.basename(__file__))
