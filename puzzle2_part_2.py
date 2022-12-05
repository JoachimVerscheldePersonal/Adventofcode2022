import pandas as pd
import numpy as np
import pathlib
import string 

move_score_dict = {0:1, 1:2, 2:3}
round_score_dict  = {0:0, 1:3, 2:6}


def read_strategy(line:str) -> tuple[int, int]:
    """
    Reads the input line and parses the string to a comparable number:
    0=Rock
    1=Paper
    2=Scissors
    """
    opponent_str = line[0]
    round_outcome_str = line[2]

    return (string.ascii_lowercase.index(opponent_str.lower()), string.ascii_lowercase.index(round_outcome_str.lower()) - string.ascii_lowercase.index('x'))


def calculate_score(opponent_move: int, round_outcome: int) -> int:
    """
    calculates both the score for the choosen move aswel as the score of the outcome of the round
    """
    winning_move = (opponent_move +1) % 3
    possible_moves = [0,1,2]

    if round_outcome == 0:
        possible_moves.remove(opponent_move)
        possible_moves.remove(winning_move)
        my_move = possible_moves[0]
    elif round_outcome == 1:
        my_move = opponent_move
    elif round_outcome == 2:
        my_move = winning_move
    else:
        raise ValueError('Value not valid')

    print(my_move)
    return round_score_dict[round_outcome] + move_score_dict[my_move]



puzzle_data_path = pathlib.Path().joinpath('data','puzzle2.txt')
total_score = 0

with puzzle_data_path.open() as f: 
    lines = f.readlines()
    for line in lines:
        opponent_move, round_outcome = read_strategy(line)
        total_score += calculate_score(opponent_move, round_outcome)


print(total_score)



        

