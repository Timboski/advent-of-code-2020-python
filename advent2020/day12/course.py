from advent2020.day12.heading import Heading
from advent2020.day12.position import Position
from advent2020.utils.read_file import ReadFile


class Course:
    def __init__(self, path: str) -> None:
        self._course = ReadFile.lines(path)

    def find_distance(self) -> int:
        position = Position(0, 0, Heading.east)
        for instruction in self._course:
            op = instruction[0]
            value = int(instruction[1:])

            if op == 'N':
                position = position.move(Heading.north, value)
            elif op == 'S':
                position = position.move(Heading.south, value)
            elif op == 'E':
                position = position.move(Heading.east, value)
            elif op == 'W':
                position = position.move(Heading.west, value)
            elif op == 'L':
                position = position.turn(-value)
            elif op == 'R':
                position = position.turn(value)
            elif op == 'F':
                position = position.move_forwards(value)
            else:
                raise ValueError(f"Unsupported instruction {instruction}")

        return abs(position.north) + abs(position.east)
