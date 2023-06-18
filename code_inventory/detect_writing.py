import cv2
import pytesseract

# Load the image
image = cv2.imread(r"Kontrol Kart 1\5RC_6007.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform thresholding or other preprocessing if needed
# ...

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Apply OCR using Tesseract
text = pytesseract.image_to_string(gray)

# Get the bounding boxes of the detected text regions
boxes = pytesseract.image_to_boxes(gray)

# Process the detected text and bounding boxes
for box in boxes.splitlines():
    print(box)

    try:
        # Extract coordinates and text content
        x, y, w, h, text = box.split(' ')
    
        # Convert coordinates to integers
        x, y, w, h = int(x), int(y), int(w), int(h)
    
        # Draw the bounding box on the image
        cv2.rectangle(image, (x, y), (w, h), (0, 255, 0), 2)
    
        # Display the text content
        print('Text:', text)
    except:
        print("Error")
# Display the image with bounding boxes
cv2.imshow('Text Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()