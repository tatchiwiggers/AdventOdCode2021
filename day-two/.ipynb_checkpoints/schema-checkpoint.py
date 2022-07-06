from dataclasses import dataclass
from typing import List

@dataclass(eq=True)
class Position:
    horizontal: int
    depth: int
    aim = 0