from __future__ import annotations

from advent2020.day12.heading import Heading


class Position:
    def __init__(self, north: int, east: int, heading: Heading) -> None:
        self.north = north
        self.east = east
        self.heading = heading

    def turn(self, degrees: int) -> Position:
        return Position(self.north, self.east, self.heading.turn(degrees))

    def move_forwards(self, dist: int) -> Position:
        return self.move(self.heading, dist)

    def move(self, heading: Heading, dist: int) -> Position:
        if heading == Heading.north:
            return self._move_north(dist)
        if heading == Heading.south:
            return self._move_south(dist)
        if heading == Heading.east:
            return self._move_east(dist)
        if heading == Heading.west:
            return self._move_west(dist)
        raise ValueError(f"Unexpected heading: {heading}")

    def _move_north(self, dist: int) -> Position:
        return Position(self.north + dist, self.east, self.heading)

    def _move_south(self, dist: int) -> Position:
        return Position(self.north - dist, self.east, self.heading)

    def _move_east(self, dist: int) -> Position:
        return Position(self.north, self.east + dist, self.heading)

    def _move_west(self, dist: int) -> Position:
        return Position(self.north, self.east - dist, self.heading)
