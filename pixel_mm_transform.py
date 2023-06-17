import numpy as np
import cv2

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

# TODO: This function may not work properly. Please check it.
def mm_to_pixel(image_path, x1, y1, x2, y2, x3, y3, x1_mm, y1_mm, x2_mm, y2_mm, x3_mm, y3_mm) -> np.ndarray:
    # Pixel coordinates of reference points
    pixel_coords = np.array([[x1, y1], [x2, y2], [x3, y3]], dtype=np.float32)

    # Real-world coordinates of reference points in millimeters
    real_coords = np.array([[x1_mm, y1_mm], [x2_mm, y2_mm], [x3_mm, y3_mm]], dtype=np.float32)

    # Calculate the perspective transformation matrix
    transformation_matrix = cv2.getAffineTransform(real_coords, pixel_coords)

    # Load the image
    image = cv2.imread(image_path)

    # Apply the perspective transformation to image coordinates
    result = cv2.warpAffine(image, transformation_matrix, (image.shape[1], image.shape[0]))

    # Return the result
    return result

def get_difference(first_image = r'Kontrol Kart 1\5RC_6009.jpg', second_image = r'Kontrol Kart 1\5RC_6007.jpg'):
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

    first_result = pixel_to_mm(first_image,x1, y1, x2, y2, x3, y3, x1_mm, y1_mm, x2_mm, y2_mm, x3_mm, y3_mm)
    cv2.imwrite(f'result_{first_image.split("/")[-1]}.jpg', first_result)

    second_result = pixel_to_mm(second_image,x1_7, y1_7, x2_7, y2_7, x3_7, y3_7, x1_mm, y1_mm, x2_mm, y2_mm, x3_mm, y3_mm)
    cv2.imwrite(f'result_{second_image.split("/")[-1]}.jpg', second_result)

    first_grey = cv2.cvtColor(first_result, cv2.COLOR_BGR2GRAY)
    second_grey = cv2.cvtColor(second_result, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(first_grey, second_grey)

    cv2.imshow('Difference', diff)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # threshold_value = 30  # Adjust this threshold value as per your needs
    # _, thresholded_diff = cv2.threshold(diff, threshold_value, 255, cv2.THRESH_BINARY)

    # cv2.imshow('Thresholded Difference', thresholded_diff)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # cv2.imwrite('thresholded_diff.jpg', thresholded_diff)

