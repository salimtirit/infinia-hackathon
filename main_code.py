import cv2
import numpy as np
import read_pap


import pandas as pd
import os
import io

folder_name = "Kontrol Kart 1"

class Component:
    def __init__(self, x, y, layer, rotation, designator):
        self.x = x
        self.y = y
        self.layer = layer
        self.rotation = rotation
        self.designator = designator
            
class Board:
    def __init__(self):
        self.component_list = []


def __find_table_start__(csv_file):
    with open(csv_file, 'r') as file:
        for line_num, line in enumerate(file):
            if len(line.strip().split(',')) > 1:  # Skip empty lines
                # Check if the line can be parsed as a CSV row
                try:
                    pd.read_csv(io.StringIO(line))
                    return line_num  # Return the line number where the table starts
                except pd.errors.ParserError:
                    continue

# returns pandas table of the exel table
def paps_to_pandas_tables():
    l = []
    for file in os.listdir(folder_name):
        if file.endswith('.csv'):
            file_path = os.path.join(folder_name, file)
            start_line = __find_table_start__(file_path)

            df = pd.read_csv(file_path,  encoding='latin1', skiprows=start_line,  skipinitialspace=True, quotechar='"') # TODO: skiprows=12 is a hack, find a better way
            print(df.head())
            l.append(df)
    return l






def calculate_conversion_factors(board: Board, pixel_x1, pixel_y1, pixel_x2, pixel_y2, mm_x1, mm_x2, mm_y1, mm_y2):
    pixel_points = [(pixel_x1, pixel_y1), (pixel_x2, pixel_y2)]  # Replace with the actual pixel coordinates
    mm_points = [(mm_x1, mm_y1), (mm_x2, mm_y2)]  # Replace with the actual millimeter coordinates

    # Calculate the conversion factors for x and y axes
    pixel_distance_x = pixel_points[1][0] - pixel_points[0][0]
    pixel_distance_y = pixel_points[1][1] - pixel_points[0][1]
    mm_distance_x = mm_points[1][0] - mm_points[0][0]
    mm_distance_y = mm_points[1][1] - mm_points[0][1]
    board.conversion_factor_x = mm_distance_x / pixel_distance_x
    board.conversion_factor_y = mm_distance_y / pixel_distance_y
    board.mm_points = mm_points
    board.pixel_points = pixel_points


def give_milimeter_coordinates(board: Board, pixel_x, pixel_y):
    mm_x = (pixel_x - board.pixel_points[0][0]) * board.conversion_factor_x + board.mm_points[0][0]
    mm_y = (pixel_y - board.pixel_points[0][1]) * board.conversion_factor_y + board.mm_points[0][1]
    return mm_x, mm_y





bb = Board()
mtx = calculate_conversion_factors(bb, 5955, 1365, 2895, 3885, 136.3308, 121.272, 17.8618, 24.2183)
x,y = give_milimeter_coordinates(bb, 1421, 3193)
a = 5






'''
def main():
    paps_list = paps_to_pandas_tables()
    for board in paps_list:
        # get pixel from user x, y 
'''
    

