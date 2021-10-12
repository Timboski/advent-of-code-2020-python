from enum import Enum


class Heading(Enum):
    north = 0
    east = 1
    south = 2
    west = 3

    def turn(self, degrees: int):
        if degrees % 90:
            raise ValueError(f"Only 90 degree turns expected, not {degrees}")
        steps = degrees // 90
        new_heading = (self.value + steps) % 4
        return Heading(new_heading)
