#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from dataIO import js
from dataIO import pk
from dataIO import textfile

data = {"name": "John", "age": 18, "favorite number": 3.1415926535,
        "hobby": ["Music", "Sport"]}

js.safe_dump(data, "data.json", indent_format=True, 
             float_precision=2, enable_verbose=True)
pk.safe_dump(data, "data.pickle", enable_verbose=True)

s = "This\nis\nPython!"
textfile.write(s, "text.txt")