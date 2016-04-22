#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
测试全C语言写成的ujson模块, IO速度最高的json模块

1. bytes type: 将bytes自动转化成字符串
2. datetime type: 将datetime转化成timestamps
3. float precision: 不支持
4. indent format: 支持
"""


from __future__ import print_function, unicode_literals

import unittest
from datetime import datetime

import ujson


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
        js = ujson.dumps(data)
        
        self.assertEqual(data["int"], ujson.loads(js)["int"])
        self.assertAlmostEqual(data["float"], ujson.loads(js)["float"], delta=0.0001)
        self.assertEqual(data["str"], ujson.loads(js)["str"])
        self.assertNotEqual(data["bytes"], ujson.loads(js)["bytes"]) # 不相等
        self.assertEqual(data["boolean"], ujson.loads(js)["boolean"])
        self.assertNotEqual(data["datetime"], ujson.loads(js)["datetime"])
        
        print(ujson.dumps(data, indent=4))


#--- Unittest ---
if __name__ == "__main__":
    unittest.main()