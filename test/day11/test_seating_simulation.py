import unittest

from advent2020.day11.seating_simulation import SeatingSimulation
from parameterized import parameterized


class TestSeatingSimulation(unittest.TestCase):
    @parameterized.expand([
        ("Example", "test/day11/example_input", 37),
        ("Regression", "advent2020/day11/input", 2152),
    ])
    def test_puzzle_1(self, test_name: str, path: str, expected_result: int):
        # Arrange
        sut = SeatingSimulation(path)

        # Act
        num = sut.occupied_seat_count()

        # Assert
        self.assertEqual(num, expected_result)

    @parameterized.expand([
        ("Example", "test/day11/example_input", 26),
        ("Regression", "advent2020/day11/input", 1937),
    ])
    def test_puzzle_2(self, test_name: str, path: str, expected_result: int):
        # Arrange
        sut = SeatingSimulation(path, alternate_strategy=True)

        # Act
        num = sut.occupied_seat_count()

        # Assert
        self.assertEqual(num, expected_result)
