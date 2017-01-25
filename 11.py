# Page: http://www.pythonchallenge.com/pc/return/5808.html
# Source doesn't show much to go on.
# Title is "odd even"
# Weird gold font HTML tag:
# 	<font color="gold" size="+1"></font>
# Split image by odd and even
# Image: http://www.pythonchallenge.com/pc/return/cave.jpg
# Developed and tested in iOS Pythonista app
# photos.pick_image() chooses from Photo library
# Image.save() saves to App's local virtual filesystem
from PIL import Image
import photos

im = photos.pick_image()
(w, h) = im.size

even = Image.new('RGB', (w // 2, h // 2))
odd = Image.new('RGB', (w // 2, h // 2))

for i in range(w):
    for j in range(h):
        p = im.getpixel((i,j))
        if (i+j)%2 == 1:
            odd.putpixel((i // 2, j // 2), p)
        else:
            even.putpixel((i // 2, j // 2), p)
even.save('even.jpg')
odd.save('odd.jpg')

even.show()
odd.show()

print("SOLUTION: http://www.pythonchallenge.com/pc/return/{}.html".format("evil"))
