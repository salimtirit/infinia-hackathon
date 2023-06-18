import cv2

x = 5950
y = 1356
label_text = "demet"

image_array = cv2.imread("5RC_6009.jpg")
# Define the font settings
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 3.5
font_color = (0, 0, 255)  # White color
thickness = 10

# Add the label to the image
image_array = cv2.putText(image_array, label_text, (x, y), font, font_scale, font_color, thickness)

# Display the image
new_width = int(image_array.shape[1] / 6)
new_height = int(image_array.shape[0] / 6)
image_array = cv2.resize(image_array, (new_width, new_height))
cv2.imshow('Labeled Image', image_array)
cv2.waitKey(0)
cv2.destroyAllWindows()