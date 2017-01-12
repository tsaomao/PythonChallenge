# Starting page: http://www.pythonchallenge.com/pc/def/oxygen.html
# Graphic with grey scale data embedded within
# Assume grey scale holds some sort of data
# Need image processing library to look at grey strip and decode some data
# values within it
# No additional info in page source
# Image URL: http://www.pythonchallenge.com/pc/def/oxygen.png
from PIL import Image

import re
import requests
from io import BytesIO
from PIL import Image

webimg = Image.open(BytesIO(requests.get("http://www.pythonchallenge.com/pc/def/oxygen.png").content))

# Get pixel values from middle row in graphic
row = [webimg.getpixel((x, webimg.height / 2)) for x in range(webimg.width)]

# Note each grey square is 7 pixels wide, so this reduces repeats
row = row[::7]

# Remove trailing non-greyscale pixels
ords = [r for r, g, b, a in row if r == g == b]

# Print out message, mapped to ASCII character set
print("".join(map(chr, ords)))

# message is:
# smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
# Rewrite to process the given numbers:
# Capture numbers in message to new nums list
nums = re.findall("\d+", "".join(map(chr, ords)))

# Translate nums list to new ASCII result
result = "".join(map(chr, map(int, nums)))

# Output to double-check
print(result)

# Format to HTTP URL
print("SOLUTION: http://www.pythonchallenge.com/pc/def/{}.html".format(result))
