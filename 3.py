import requests
import re

url = 'http://www.pythonchallenge.com/pc/def/equality.html'
r = requests.get(url)
# Exactly 3 upper case letters on either side of a lower case letter
pattern = '[^A-Z][A-Z]{3}([a-z]{1})[A-Z]{3}[^A-Z]'

hits = re.findall(pattern, r.text)

urlpart = "".join(hits)

print("http://www.pythonchallenge.com/pc/def/{}.html".format(urlpart))

print("http://www.pythonchallenge.com/pc/def/{}.php".format(urlpart))
