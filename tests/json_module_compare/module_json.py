#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
测试标准库中的json模块

1. bytes type: 不支持
2. datetime type: 不支持
3. float precision: 支持
4. indent format: 支持
"""


from __future__ import print_function, unicode_literals

import unittest
import json
from json import encoder
from datetime import datetime


encoder.FLOAT_REPR = lambda x: format(x, ".2f")


class Unittest(unittest.TestCase):
    def test_all(self):
        data = {
            "int": 100,
            "float": 3.1415926535,
            "str": "string example 字符串例子",
            "boolean": True,
        }
        js = json.dumps(data)

        self.assertEqual(data["int"], json.loads(js)["int"])
        self.assertAlmostEqual(data["float"], json.loads(js)[
                               "float"], delta=0.0001)
        self.assertEqual(data["str"], json.loads(js)["str"])
        self.assertEqual(data["boolean"], json.loads(js)["boolean"])

        print(json.dumps(data, sort_keys=True, indent=4))


#--- Unittest ---
if __name__ == "__main__":
    unittest.main()
