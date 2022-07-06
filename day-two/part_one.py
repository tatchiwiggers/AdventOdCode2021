from schema import Position
from typing import List
import csv


with open('input.txt') as movs:
    csv_reader = csv.reader(movs, delimiter=',')
    
    movs = [row[0] for row in csv_reader]
    

def get_position(instructions: List[str]) -> Position:
    result = Position(horizontal=0, depth=0)
    
    for instruction in instructions:
        direction, value = instruction.split()
        if direction == "forward":
            result.horizontal += int(value)
        elif direction == "down":
            result.depth += int(value)
        else:
            result.depth -= int(value)

    return result.horizontal * result.depth

print('P-one', get_position(movs))