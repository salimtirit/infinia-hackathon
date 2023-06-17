import numpy as np
import cv2

#r109
x1, y1 = 5950, 1356
x1_mm, y1_mm = 136.3308, 121.272

#r132
x2, y2 = 2889, 3876
x2_mm, y2_mm = 17.8618, 24.2183

#r30
x3, y3 = 3229, 1530
x3_mm, y3_mm = 31.1, 114.575

#left_up
# 0,0

#right_down
# 8192, 5464

# Pixel coordinates of reference points
pixel_coords = np.array([[x1, y1], [x2, y2], [x3, y3]], dtype=np.float32)

# Real-world coordinates of reference points in millimeters
real_coords = np.array([[x1_mm, y1_mm], [x2_mm, y2_mm], [x3_mm, y3_mm]], dtype=np.float32)

# Calculate the perspective transformation matrix
transformation_matrix = cv2.getAffineTransform(pixel_coords, real_coords)

# Load the image
image = cv2.imread(r'Kontrol Kart 1\5RC_6009.jpg')

# Apply the perspective transformation to image coordinates
result = cv2.warpAffine(image, transformation_matrix, (image.shape[1], image.shape[0]))

# Display the result or save it to a file
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()