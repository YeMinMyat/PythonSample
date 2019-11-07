from __future__ import print_function
from PIL import  Image,ImageColor

im = Image.open("cat.webp").convert("L")
print(im.format, im.size, im.mode)

im.show()

