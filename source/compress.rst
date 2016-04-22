compress utility module
=======================
First, import the module::

	from dataIO import compress

Read compressed binary in and out from file is easy::

	binary = b"Hello World"

	compress.write_gzip(binary, "data.gz")

	binary = compress.read_gzip("data.gz")

If you want to **shorten and compress** your string::

	text = "This is a very long string: abcdefghijk ..." * 10
	compressed_text = compress.compress_str(text)
	decompressed_text = compress.decompress_str(compressed_text)

Elegant, Ha?