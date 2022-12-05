import pandas as pd
import numpy as np
import pathlib
import string 
import copy

puzzle_data_path = pathlib.Path().joinpath('data','puzzle3.txt')
priority_dict = string.ascii_lowercase
priority_sum = 0

def split_compartements(line: str) -> tuple[str, str]:
    line_length = len(line)
    split_position = int(line_length/2)
    return line[0:split_position], line[split_position:]

def get_rucksack_intersection(rucksack1: str, rucksack2: str) -> str:
    return set([item for item in rucksack1 if item in rucksack2])

def get_group_intersection(group: list[str])-> str:
    intersection1 = get_rucksack_intersection(group[0], group[1])
    return get_rucksack_intersection(list(intersection1), group[-1])

def get_groups(lines: list[str]) -> tuple[str,str,str]:
    return [lines[n:n+3] for n in range(0, len(lines), 3)]

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
    for group in get_groups(lines):
        intersecting_items = get_group_intersection(group)
        priority_sum += get_rucksack_priority_sum(intersecting_items)
        
    print(priority_sum)




        

