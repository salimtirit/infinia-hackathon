import cv2
import numpy as np

# Load the two images
image1 = cv2.imread('5RC_6007.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('5RC_6009.jpg', cv2.IMREAD_GRAYSCALE)

# Initialize SIFT
sift = cv2.SIFT_create()

# Detect keypoints and compute descriptors for the images
keypoints1, descriptors1 = sift.detectAndCompute(image1, None)
keypoints2, descriptors2 = sift.detectAndCompute(image2, None)

# Initialize a FLANN-based matcher
matcher = cv2.FlannBasedMatcher()

# Match keypoints between the images
matches = matcher.match(descriptors1, descriptors2)

# Filter matches based on distance
matches = sorted(matches, key=lambda x: x.distance)
good_matches = matches[:50]  # Adjust the number of good matches as needed

# Estimate the transformation between the images
src_pts = np.float32([keypoints1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

# Apply the estimated transformation to align the images
aligned_image2 = cv2.warpPerspective(image2, M, (image1.shape[1], image1.shape[0]))

# Calculate the absolute difference between the aligned images
difference = cv2.absdiff(image1, aligned_image2)

# Display the difference image
cv2.imshow('Differenceasd.png', difference)
cv2.waitKey(0)
cv2.destroyAllWindows()
