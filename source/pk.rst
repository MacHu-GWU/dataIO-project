pickle utility module
=====================
First, import the module::

	from dataIO import pk

Create a dummy data::

	data = {"name": "John", "age": 20, "favorite number": 3.1415926535}

Dump to file::

	# by default overwrite is False, to prevent you overwrite existing file
	pk.dump(data, "data.pickle", overwrite=False)

	# by default it use your python version as the pickle protocol
	# but you can always using 2 for python2/3 IO compatibility
	pk.dump(data, "data.pickle", pk_protocol=2)

	# by default enable_versose is True, if you don't want help information
	# you can close it
	pk.dump(data, "data.pickle", enable_versose=False)

Dump and compress::

	# you just need to change the file extension to .gz
	pk.dump(data, "data.pickle.gz")

**If while you are overwriting existing file, it is been interrupted by some reason, then it left a incomplete file, and also you lose your old file!** I believe you absolute wants to avoid that. In other word, **you want atomic write** (It fail, otherwise 100% complete), you can use :meth:`~dataIO.pk.safe_dump` instead::

	pk.safe_dump(data, "data.pickle")

Load from file::

	data = pk.load("data.pickle")

If you want a default value when data file not exist, you can do this::

	data = pk.load("data.pickle", default=dict())

You can easily use pickle to **convert any python picklable object to url safe string**, so you can **put it in database or transfer data via url**

.. code-block:: python

	class Person(object):
	    def __init__(self, name)
	        self.name = name

All you need is::

	text = pk.obj2str(person)

This is when you need it back::

	person = pk.str2obj(text)