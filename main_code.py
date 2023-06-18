import cv2
import numpy as np
from read_pap import *
from pixel_mm_transform import *
import classes


'''
jpg image format is a compressed format, so this will yield diff even for identically taken photos
'''


def label_board_image(image_array, board):
    for component in board.component_list:
        x,y = mm_to_pixel(component.x,component.y, board)
        x = int(component.x) * 10
        y = int(component.y) * 10
        print(f"x: {x}, y:{y}")
        label_text = component.designator

        # Define the font settings
        font_scale = 1
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_color = (0, 255, 0)  # White color
        thickness = 1

        # Add the label to the image
        image_array = cv2.putText(image_array, label_text, (x, y), font, font_scale, font_color, thickness)

        # Display the image
    new_width = int(image_array.shape[1] / 6)
    new_height = int(image_array.shape[0] / 6)
    image_array = cv2.resize(image_array, (new_width, new_height))
    cv2.imwrite('Labeled Image.png', image_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    



a = paps_to_pandas_tables()
label_board_image(pixel_to_mm("5RC_6007.jpg", a["Ahbap_PCB"]), a["Ahbap_PCB"])




'''
def main():
    paps_list = paps_to_pandas_tables()
    for board in paps_list:
        # get pixel from user x, y 
'''