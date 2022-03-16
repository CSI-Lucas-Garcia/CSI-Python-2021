 import requests
>>> res = requests.get("https://www.gutenberg.org/cache/epub/67619/pg67619.txt")
>>> type(res)
<class 'requests.models.Response'>
>>> res.status_code ==requests.codes.ok
True
>>> len(res.text)
657850
>>> print(res.text[:300])