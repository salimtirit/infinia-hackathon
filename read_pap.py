import pandas as pd
import os
import io

folder_name = "Kontrol Kart 1"

def find_table_start(csv_file):
    with open(csv_file, 'r') as file:
        for line_num, line in enumerate(file):
            print(line_num)
            print(line)
            print(len(line.strip()))
            if line.strip():  # Skip empty lines
                # Check if the line can be parsed as a CSV row
                try:
                    pd.read_csv(io.StringIO(line))
                    return line_num  # Return the line number where the table starts
                except pd.errors.ParserError:
                    continue


for file in os.listdir(folder_name):
    if file.endswith('.csv'):
        print(file)
        file_path = os.path.join(folder_name, file)
        print(file_path)
        start_line = find_table_start(file_path)
        df = pd.read_csv(file_path,  encoding='latin1', skiprows=start_line) # TODO: skiprows=12 is a hack, find a better way
        print(df.head())