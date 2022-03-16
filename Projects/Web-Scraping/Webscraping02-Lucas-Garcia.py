import requests
res = requests.get("https://www.gutenberg.org/cache/epub/67637/pg67637.txt")
res.raise_for_status()
playFile = open("Acient Greece Volume II","wb")
for chunk in res.iter_content(10000):
    playFile.write(chunk)
playFile.close()