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
        x = int(component.x)
        y = int(component.y)
        label_text = component.designator

        # Define the font settings
        font_scale = 3.5
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_color = (0, 0, 255)  # White color
        thickness = 10
        thickness = 2

        # Add the label to the image
        image_array = cv2.putText(image_array, label_text, (x, y), font, font_scale, font_color, thickness)

        # Display the image
    new_width = int(image_array.shape[1] / 6)
    new_height = int(image_array.shape[0] / 6)
    image_array = cv2.resize(image_array, (new_width, new_height))
    cv2.imshow('Labeled Image', image_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    



a = paps_to_pandas_tables()
label_board_image(cv2.imread("5RC_6007.jpg", cv2.IMREAD_GRAYSCALE), a["Ahbap_PCB"])




'''
def main():
    paps_list = paps_to_pandas_tables()
    for board in paps_list:
        # get pixel from user x, y 
'''