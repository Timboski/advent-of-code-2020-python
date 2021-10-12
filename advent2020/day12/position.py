from __future__ import annotations

from advent2020.day12.heading import Heading


class Position:
    def __init__(self, north: int, east: int, heading: Heading = None) -> None:
        self.north = north
        self.east = east
        self.heading = heading

    def turn(self, degrees: int) -> Position:
        return Position(self.north, self.east, self.heading.turn(degrees))

    def rotate(self, degrees: int) -> Position:
        north_dir = Heading.north.turn(degrees)
        east_dir = Heading.east.turn(degrees)
        return Position(0, 0).move(north_dir, self.north).move(east_dir, self.east)

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

    def move_towards_waypoint(self, waypoint: Position, times: int) -> Position:
        mid = self._move_north(waypoint.north * times)
        return mid._move_east(waypoint.east * times)

    def _move_north(self, dist: int) -> Position:
        return Position(self.north + dist, self.east, self.heading)

    def _move_south(self, dist: int) -> Position:
        return Position(self.north - dist, self.east, self.heading)

    def _move_east(self, dist: int) -> Position:
        return Position(self.north, self.east + dist, self.heading)

    def _move_west(self, dist: int) -> Position:
        return Position(self.north, self.east - dist, self.heading)
