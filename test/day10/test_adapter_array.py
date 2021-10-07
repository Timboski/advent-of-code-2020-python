import unittest

from advent2020.day10.adapter_array import AdapterArray
from parameterized import parameterized


class TestAdapterArray(unittest.TestCase):
    @parameterized.expand([("Example 1", "test/day10/example_input_1", 35),
                           ("Example 2", "test/day10/example_input_2", 220),
                           ("Regression", "advent2020/day10/input", 2450)])
    def test_puzzle_1(self, test_name: str, path: str, expected_result: int):
        # Arrange
        sut = AdapterArray(path)

        # Act
        num = sut.find_sum()

        # Assert
        self.assertEqual(num, expected_result)

    @parameterized.expand([("Example 1", "test/day10/example_input_1", 8),
                           ("Example 2", "test/day10/example_input_2", 19208)])
    def test_puzzle_2(self, test_name: str, path: str, expected_result: int):
        # Arrange
        sut = AdapterArray(path)

        # Act
        num = sut.find_num_combinations()

        # Assert
        self.assertEqual(num, expected_result)
