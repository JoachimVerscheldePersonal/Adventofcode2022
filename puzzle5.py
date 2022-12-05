import pandas as pd
import numpy as np
import pathlib
import string 

puzzle_data_path = pathlib.Path().joinpath('data','puzzle5.txt')

crate_stack_rows = []
crate_stacks = []

def get_next_crate(crate_stack_line: str):
    while len(crate_stack_line) >= 3:
        crate = crate_stack_line[0:3]
        crate_stack_line = crate_stack_line[4:]
        
        crate = crate.lstrip('[')
        crate = crate.rstrip(']')
        crate = crate.strip()

        yield crate if crate else None

def build_crate_stack(crate_stack_rows: list[list[str]]) -> list[list[str]]:
    stacks = []
    number_of_stacks = len(crate_stack_rows[0])

    for i in range(number_of_stacks):
        stack = []
        for row in crate_stack_rows:
            if row[i]:
                stack.append(row[i])

        stacks.append(stack)

    return stacks

def get_crate_rows(crate_stack_lines: list[str]) -> list[list[str]]:
    rows = []
    for crate_stack_line in crate_stack_lines:
        row = [crate for crate in get_next_crate(crate_stack_line)]
        rows.append(row)
    rows.reverse()
    return rows

def parse_instruction_line(instruction_line: str) -> tuple[int,int,int]:
    numbers = [int(number) for number in instruction_line.split() if number.isdigit()]
    numbers[-2] -=1
    numbers[-1] -=1
    return tuple(numbers)

def execute_instruction(number_of_crates: int, from_stack:int , to_stack: int):
    crates_to_move = [crate_stacks[from_stack].pop() for i in range(number_of_crates)]
    crate_stacks[to_stack].extend(crates_to_move)

def get_top_crates() -> str:
    top_crates = ''.join([stack[-1] for stack in crate_stacks])
    return top_crates

with puzzle_data_path.open() as f: 
    
    lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    crate_stack_lines = [line for line in lines if line.find('[') == 0]
    instruction_lines = [line for line in lines if line.find('m') == 0]
    crate_stack_rows = get_crate_rows(crate_stack_lines)
    crate_stacks = build_crate_stack(crate_stack_rows)
    
    for instruction_line in instruction_lines:
        number_of_crates, from_stack , to_stack = parse_instruction_line(instruction_line)
        execute_instruction(number_of_crates, from_stack, to_stack)

print(get_top_crates())
   




        

