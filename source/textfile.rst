textfile utility module
=======================
First, import the module::

	from dataIO import textfile

Having encoding problem in Python2? Do this::

	text = "English, 中文, にほんご, ру́сский язы́к, ..."
	textfile.write(text, "text.txt") # write
	text = textfile.read("text.txt") # read

If you have a file with special encoding, do this::

	text = textfile.read("text.txt", encoding="Your encoding")

**If you don't know the encoding**, you can let ``dataIO`` smartly decided for you. This feature requires ``chardet``, just do ``pip install chardet``.

::

	text = textfile.smartread("text.txt")

Have lots of text file downloaded from Internet, but the encoding is messed up? You can easily encode them to utf-8 by doing this::

	to_utf8("download.txt") # automatically generate a new file, you never lose your old file.

You probably need `skip first M lines, and fetch next N lines` read patter, and you don't want to read a super big file into your memory, now you should do this::

	# skip first 2 lines, fetch next 1000 lines
	for line in textfile.readlines("text.txt", skiplines=2, nlines=1000, strip="right"):
	    print(line) # do what ever you want with this line

For parameter explanation, read this :meth:`~dataIO.textfile.readlines`

``readchunks`` method doing similar things. The only difference is reading multiple line at a time as a chunk, then yield. Here's a example usage::
	
	Group ID, Series ID
	1, 1
	1, 2
	1, 3
	2, 1
	2, 2
	2, 3
	3, 1
	3, 2
	3, 3

Then you can do this::

	for chunk in textfile.readchunks("text.txt", skiplines=1, chunksize=3):
	    print(chunk) # do what ever you want with this chunk