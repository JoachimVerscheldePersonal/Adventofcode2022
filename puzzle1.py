import pandas as pd
import numpy as np
import pathlib

calories = []

puzzle_data_path = pathlib.Path().joinpath('data','puzzle1.txt')

calories_count = 0

with puzzle_data_path.open() as f: 
    lines = f.readlines()
    for line in lines:
        
        if line == '\n':
            calories.append(calories_count)
            calories_count = 0
        else:
            calories_count += int(line)



print(max(calories))