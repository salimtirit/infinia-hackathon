import numpy as np
import cv2

#r109
x1, y1 = 5950, 1356
x1_7, y1_7 = 5914, 1356
x1_mm, y1_mm = 1363.308, 1212.72

#r132
x2, y2 = 2889, 3876
x2_7, y2_7 = 2954, 3775
x2_mm, y2_mm = 178.618, 242.183

#r30
x3, y3 = 3229, 1530
x3_7, y3_7 = 3286, 1515
x3_mm, y3_mm = 311, 1145.75

#left_up
# 0,0

#right_down
# 8192, 5464

def pixel_to_mm(image_path, x1, y1, x2, y2, x3, y3, x1_mm, y1_mm, x2_mm, y2_mm, x3_mm, y3_mm) -> np.ndarray:
    # Pixel coordinates of reference points
    pixel_coords = np.array([[x1, y1], [x2, y2], [x3, y3]], dtype=np.float32)

    # Real-world coordinates of reference points in millimeters
    real_coords = np.array([[x1_mm, y1_mm], [x2_mm, y2_mm], [x3_mm, y3_mm]], dtype=np.float32)

    # Calculate the perspective transformation matrix
    transformation_matrix = cv2.getAffineTransform(pixel_coords, real_coords)

    # Load the image
    image = cv2.imread(image_path)

    # Apply the perspective transformation to image coordinates
    result = cv2.warpAffine(image, transformation_matrix, (image.shape[1], image.shape[0]))

    # Return the result
    return result

# result = pixel_to_mm(r'Kontrol Kart 1\5RC_6009.jpg',x1, y1, x2, y2, x3, y3, x1_mm, y1_mm, x2_mm, y2_mm, x3_mm, y3_mm)
# cv2.imwrite('result_deneme.jpg', result)