import numpy as np
from PIL import Image, ImageOps
from numpy import asarray

image = Image.open('five.jpg')
new_image = image.resize((28,28))
inverted_image = ImageOps.invert(new_image)

pixels = asarray(inverted_image)

result_arr = []

for i in pixels:
    for j in i:
        result_arr.append(int(np.sum(j)/3))

print(result_arr)