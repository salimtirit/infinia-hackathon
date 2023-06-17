import os
import pandas as pd
from main_code import Board
import io


folder_name = "Kontrol Kart 1"

# helper for next function
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
    dict = {}
    for file in os.listdir(folder_name):
        if file.endswith('.csv'):
            file_path = os.path.join(folder_name, file)
            start_line = __find_table_start__(file_path)

            df = pd.read_csv(file_path,  encoding='latin1', skiprows=start_line,  skipinitialspace=True, quotechar='"') # TODO: skiprows=12 is a hack, find a better way
            print(df.head())
            board = Board(df)
            name_of_board = file.replace("Pick Place for ", "")
            name_of_board = name_of_board.replace(".csv", "")
            dict[name_of_board] = board
    return dict