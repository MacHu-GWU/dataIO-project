#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from docfly import Docfly
import shutil
 
try:
    shutil.rmtree(r"source\dataIO")
except Exception as e:
    print(e)
     
docfly = Docfly("dataIO", dst="source", 
    ignore=[
        "dataIO.zzz_manual_install.py",
        "dataIO.tests",
    ]
)
docfly.fly()
