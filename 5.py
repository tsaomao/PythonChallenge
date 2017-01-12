# From source of http://www.pythonchallenge.com/pc/def/peak.html
# File at http://www.pythonchallenge.com/pc/def/banner.p appears to be a
# Python pickle (serialized object)
# Implement an unpickler to see what's in there.
# Warning: not proof against malicious code
from urllib.request import urlopen
import pickle

url = "http://www.pythonchallenge.com/pc/def/banner.p"

pickle_web = urlopen(url)

raw_data = pickle.load(pickle_web)

for line in raw_data:
	print("".join([a * b for a, b in line]))

# output is banner printed "channel"
print ("http://www.pythonchallenge.com/pc/def/{}.html".format("channel"))

