import cv2
import numpy as np

# Load the grayscale images
image1 = cv2.imread('5RC_6009.jpg')
image2 = cv2.imread('5RC_6007.jpg')

image1_bw = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image2_bw = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)


# Initialize ORB feature detector
orb = cv2.ORB_create()

# Find keypoints and descriptors in the images
keypoints1, descriptors1 = orb.detectAndCompute(image1, None)
keypoints2, descriptors2 = orb.detectAndCompute(image2, None)

# Initialize Brute-Force Matcher
matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match keypoints in the images
matches = matcher.match(descriptors1, descriptors2)

# Sort matches by distance (lower is better)
matches = sorted(matches, key=lambda x: x.distance)

# Keep only the top N matches (adjust N according to your needs)
N = 100
matches = matches[:N]

# Extract matched keypoints
src_points = np.float32([keypoints1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
dst_points = np.float32([keypoints2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

# Estimate the transformation matrix using RANSAC
transformation_matrix, _ = cv2.findHomography(src_points, dst_points, cv2.RANSAC, 5.0)

# Warp the second image to align with the first image
aligned_image2 = cv2.warpPerspective(image2, transformation_matrix, (image1.shape[1], image1.shape[0]))

# Calculate the absolute difference between the aligned images
diff = cv2.absdiff(image1, aligned_image2)

#diff = 255 - cv2.absdiff(diff, image1)
diff = 255 - cv2.absdiff(diff, image2)

# Display the difference image
cv2.imwrite('Difference Image.png', diff)


