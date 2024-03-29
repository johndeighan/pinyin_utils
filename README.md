# README.md

Utilities for handling Chinese pinyin

The utilities in this library make it easy to use
Chinese pinyin

The unit tests are directly in the files and therefore
serve as documentation of the utility functions in it.
To execute the unit tests, you can just run:

	pytest -s pinyin_utils.py

To get the library into a project:

	pip install pinyin_utils

# SYNOPSIS of pinyin_utils.py

coming soon

# SYNOPSIS of translate.py

```python
import os, time, trio, asks, pprint

from translate import translate, initDB, setApiKey

async def main():

	# --- The database need not exist.
	#     Furthermore, if you leave out this call,
	#     the database will be put at ./Translations.db by default
	initDB('./Translations.db')

	# --- This env var key is the default if you leave this out
	setApiKey(os.environ['GOOGLE_APIKEY'])

	hWords = {
		'cat': None,
		'dog': None,
		}

	start_time = time.time()
	async with trio.open_nursery() as nursery:
		nursery.start_soon(translate, hWords)
	total = time.time() - start_time
	print(f"Total time: {total}")

	pprint.PrettyPrinter(indent=3).pprint(hWords)

asks.init('trio')
trio.run(main)

# SYNOPSIS of tabdb.py

	coming soon

# SYNOPSIS of englishWords.py

	coming soon

# SYNOPSIS of ChineseDB.py

	coming soon

