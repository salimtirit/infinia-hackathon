import cv2
import numpy as np
import read_pap
import pixel_mm_transform



'''
jpg image format is a compressed format, so this will yield diff even for identically taken photos
'''


class Component:
    def __init__(self, x, y, layer, rotation, designator):
        self.x = x
        self.y = y
        self.layer = layer
        self.rotation = rotation
        self.designator = designator
            
class Board:
    def __init__(self, pandas_data_frame):
        self.component_list = []
        for _, row in pandas_data_frame.iterrows():
            designator = row['Designator']
            x = row['Center-X(mm)']
            y = row['Center-Y(mm)']
            layer = row['Layer']
            rotation = row['Rotation']
            
            layer = True
            if layer != "TopLayer":
                layer = False

            c = Component(x,y,layer,rotation,designator)
            self.component_list.append(c)



def label_board_image(image_array, board):
    for component in board.component_list:
        x,y = mm_to_pixel(component.x, component.y) #TODO: writ this function
    





'''
def main():
    paps_list = paps_to_pandas_tables()
    for board in paps_list:
        # get pixel from user x, y 
'''
    

