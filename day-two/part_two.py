from schema import Position
from typing import List
import csv

with open('input.txt') as movs:
    csv_reader = csv.reader(movs, delimiter=',')
    
    movs = [row[0] for row in csv_reader]

def get_position2(instructions: List[str]) -> Position:
    result = Position(horizontal=0, depth=0)

    for instruction in instructions:
        direction, amount = instruction.split()
        if direction == "forward":
            result.horizontal += int(amount)
            result.depth += result.aim * int(amount)
        elif direction == "down":
            result.aim += int(amount)
        elif direction == "up":
            result.aim -= int(amount)

    return result.horizontal * result.depth


print(get_position2(movs))

