#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
测试MongoDB的Python API模块pymongo中自带的bson模块。

1. bytes type: 完美支持
2. datetime type: 完美支持
3. float precision: 支持
4. indent format: 支持

在Python社区, 我所熟悉的json模块有三个:

1. json: Python标准库自带, 无需安装
2. ujson: 用纯C语言写的json, 速度最快
3. bson: MongoDB的Python API模块pymongo中自带的bson (binary json)模块, 功能最全

综上所述, 建议使用bson进行与json有关的工作。
"""


from __future__ import print_function, unicode_literals

import unittest
from json import encoder
from datetime import datetime

from bson import json_util


encoder.FLOAT_REPR = lambda x: format(x, ".2f")


class Unittest(unittest.TestCase):
    def test_all(self):
        data = {
            "int": 100,
            "float": 3.1415926535,
            "str": "string example 字符串例子",
            "bytes": "bytes example 比特串例子".encode("utf-8"),
            "boolean": True,
            "datetime": datetime.now()
        }
        js = json_util.dumps(data)

        data1 = json_util.loads(js)
        self.assertEqual(data["int"], data1["int"])
        self.assertAlmostEqual(data["float"], data1["float"], delta=0.0001)
        self.assertEqual(data["str"], data1["str"])
        self.assertEqual(data["boolean"], data1["boolean"])

        print(data1["bytes"])
        print(data1["datetime"])
        print(json_util.dumps(data, sort_keys=True, indent=4))


#--- Unittest ---
if __name__ == "__main__":
    unittest.main()
