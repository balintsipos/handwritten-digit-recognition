import imageio
import matplotlib.pyplot as plt
import numpy as np


# result = []
# for i in range(784):
#     result.append(1)

# print(result)


from PIL import Image
image = Image.open('five.jpg')
new_image = image.resize((28,28))

from numpy import asarray
data = asarray(new_image)
print(len(data[0]))