from enum import Enum


class Heading(Enum):
    north = 0
    east = 1
    south = 2
    west = 3

    def turn(self, degrees: int):
        steps = degrees // 90
        new_heading = (self.value + steps) % 4
        return Heading(new_heading)
