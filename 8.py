# Starting URL: http://www.pythonchallenge.com/pc/def/integrity.html
# Clicking insect pops up an authentication box
# Viewing source shows interesting data here:
# <!--
# un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
# -->
# Googling 'BZh91AY&S', longest string in common between "un" and "pw" strings,
# Yields this good looking hit: http://effbot.org/librarybook/bz2.htm
# Indicates "un"/"username" and "pw"/"password" are probably bz2-encoded
# strings.
import bz2
import re

bun = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
bpw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

print("Username: " + re.findall("b'(.*)'", str(bz2.decompress(bun)))[0])
print("Password: " + re.findall("b'(.*)'", str(bz2.decompress(bpw)))[0])

print("SOLUTION: Go to URL: http://www.pythonchallenge.com/pc/def/integrity.html")
print("SOLUTION: Click insect in picture. Input username and password at prompt")
