import pandas as pd
import numpy as np
import pathlib
import string 


puzzle_data_path = pathlib.Path().joinpath('data','puzzle3.txt')
priority_dict = string.ascii_lowercase
priority_sum = 0

def split_compartements(line: str) -> tuple[str, str]:
    line_length = len(line)
    split_position = int(line_length/2)
    return line[0:split_position], line[split_position:]

def get_items_intersection(compartement1: str, compartement2: str) -> str:
    return set([item for item in compartement1 if item in compartement2])

def get_rucksack_priority_sum(intersecting_items: str) -> int:
    if not intersecting_items:
        return 0

    lowercase_priorities = [string.ascii_lowercase.index(item) + 1 for item in intersecting_items if item.islower()]
    uppercase_priorities = [string.ascii_uppercase.index(item) + 27 for item in intersecting_items if item.isupper()]
    lower_case_sum = sum(lowercase_priorities)
    uppercase_sum = sum(uppercase_priorities)
    return lower_case_sum + uppercase_sum

with puzzle_data_path.open() as f: 
    lines = f.readlines()
    for line in lines:
        compartement1, compartement2 = split_compartements(line)
        intersecting_items = get_items_intersection(compartement1, compartement2)
        priority_sum += get_rucksack_priority_sum(intersecting_items)
        
    print(priority_sum)




        

