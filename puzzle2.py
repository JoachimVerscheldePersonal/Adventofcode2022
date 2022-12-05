import pandas as pd
import numpy as np
import pathlib
import string 

move_score_dict = {0:1, 1:2, 2:3}
winning_move_dict  = {0:1, 1:2, 2:0}


def read_strategy(line:str) -> tuple[int, int]:
    """
    Reads the input line and parses the string to a comparable number:
    0=Rock
    1=Paper
    2=Scissors
    """
    opponents_move_str = line[0]
    my_move_str = line[2]
    return (string.ascii_lowercase.index(opponents_move_str.lower()), string.ascii_lowercase.index(my_move_str.lower()) - string.ascii_lowercase.index('x'))


def calculate_score(opponents_move: int, my_move: int) -> int:
    """
    calculates both the score for the choosen move aswel as the score of the outcome of the round
    """
    move_score = move_score_dict[my_move]
    round_score = 0
    if my_move == opponents_move:
        round_score = 3
    elif winning_move_dict[opponents_move] == my_move:
        round_score = 6
    
    return move_score + round_score



puzzle_data_path = pathlib.Path().joinpath('data','puzzle2.txt')
total_score = 0

with puzzle_data_path.open() as f: 
    lines = f.readlines()
    for line in lines:
        opponents_move, my_move = read_strategy(line)
        total_score += calculate_score(opponents_move, my_move)


print(total_score)



        

