import pandas as pd
import numpy as np
import pathlib
import string 


puzzle_data_path = pathlib.Path().joinpath('data','puzzle4.txt')
number_of_pairs = 0


def get_sections(line: str) -> tuple[set[int], set[int]]:
    groups = line.split(sep=',')
    group1 = get_section(group=groups[0])
    group2 = get_section(group=groups[1])
    return group1, group2

def get_section(group: str):
    limits = group.split(sep='-')
    limits_int = [int(item) for item in limits]
    return set(range(limits_int[0], limits_int[1]+1))

with puzzle_data_path.open() as f: 
    lines = f.readlines()
    for line in lines:
       group1, group2 = get_sections(line)
       if group1.issubset(group2) or group2.issubset(group1):
        number_of_pairs += 1


print(number_of_pairs)
   




        

