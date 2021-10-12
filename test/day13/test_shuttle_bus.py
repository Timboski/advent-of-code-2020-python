import unittest

from advent2020.day13.shuttle_bus import ShuttleBus
from parameterized import parameterized


class TestShuttleBus(unittest.TestCase):
    @parameterized.expand([
        ("Example", "test/day13/example_input", 295),
    ])
    def test_puzzle_1(self, test_name: str, path: str, expected_result: int):
        # Arrange
        sut = ShuttleBus(path)

        # Act
        ans = sut.puzzle_1()

        # Assert
        self.assertEqual(ans, expected_result)
