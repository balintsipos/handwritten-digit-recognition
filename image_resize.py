import numpy as np

# result = []
# for i in range(784):
#     result.append(1)

# print(result)


from PIL import Image, ImageOps
image = Image.open('five.jpg')
new_image = image.resize((28,28))
inverted_image = ImageOps.invert(new_image)

from numpy import asarray
pixels = asarray(inverted_image)

result_arr = []

for i in pixels:
    for j in i:
        result_arr.append(int(np.sum(j)/3))

print(len(result_arr))