from PIL import Image
import numpy as np

# Read the original image
img = Image.open("5RC_6009.jpg")

# Make image to numpy array
img = np.array(img)

print(img.shape)

# Make the pixels between 0,0 and 10, 10 red
img[1360:1370,5950:5960, 0] = 255
img[1360:1370,5950:5960, 1] = 0
img[1360:1370,5950:5960, 2] = 0

img[3880:3900, 2880:2890,  0] = 255
img[3880:3900, 2880:2890,  1] = 0
img[3880:3900, 2880:2890,  2] = 0

# show the image
from matplotlib import pyplot as plt
plt.imshow(img)
plt.show()
