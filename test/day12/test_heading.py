import unittest

from advent2020.day12.heading import Heading
from parameterized import parameterized


class TestHeading(unittest.TestCase):
    @parameterized.expand([
        ("TurnLeft", Heading.north, -90, Heading.west),
        ("TurnRight", Heading.north, 90, Heading.east),
        ("TurnAround", Heading.east, 180, Heading.west),
        ("FullCircle", Heading.south, 360, Heading.south),
        ("BigLeft", Heading.south, -450, Heading.east),
        ("BigRight", Heading.west, 810, Heading.north),
    ])
    def test_turns(self, test_name: str, initial_heading: Heading, degrees: int,
                   expected_heading: Heading):
        # Arrange
        sut = Heading(initial_heading)

        # Act
        new_heading = sut.turn(degrees)

        # Assert
        self.assertEqual(new_heading, expected_heading)
