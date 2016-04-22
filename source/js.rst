json utility module
===================
First, import the module::

	from dataIO import js

Create a dummy data::

	data = {"name": "John", "age": 20, "favorite number": 3.1415926535}

Dump to file::

	# by default overwrite is False, to prevent you overwrite existing file
	js.dump(data, "data.json", overwrite=False)

	# by default indent_format is False, it's faster, but not human readable
	js.dump(data, "data.json", indent_format=True)

	# by default it keeps all float decimal. You can name how much you want to keep
	js.dump(data, "data.json", float_precision=2)

	# by default enable_versose is True, if you don't want help information
	# you can close it
	js.dump(data, "data.json", enable_versose=False)

Dump and compress::

	# you just need to change the file extension to .gz
	js.dump(data, "data.json.gz")

**If you are overwriting existing file, and sometime it is interrupted by some reason, you don't want a incomplete file. In other word, **you want atomic write** (It fail, otherwise 100% complete)**, you can use :meth:`~dataIO.js.safe_dump`::

	js.safe_dump(data, "data.json")

Load from file::

	data = js.load("data.json")

If you **want a default value when data file not exist**, you can do this::

	data = js.load("data.json", default=dict())

If your data is json serializable, you can **pretty print** it::

	js.pprint(data)

At the end, **I strongly recommend to install** ``pymongo``. Why? Because there's a ``bson`` along with ``pymongo``, and that is the most stable and compatible json extension in the community. (Because there's a enterprise - 10gen, MongoDB company behind this) **It compatible with** ``datetime`` and ``bytes`` datatype, and **perfectly support indent format and float precision**. ``dataIO`` doens't require ``bson``, but you should try this for better features.