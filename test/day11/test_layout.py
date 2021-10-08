import unittest

from advent2020.day11.layout import Layout
from parameterized import parameterized


class TestLayout(unittest.TestCase):
    @parameterized.expand([("example_input"), ("example_round_1")])
    def test_is_same_state(self, input_file: str):
        # Arrange
        test_path = "test/day11/"
        sut = Layout.from_file(test_path + input_file)
        other = Layout.from_file(test_path + input_file)

        # Act
        res = sut.is_same_state(other)

        # Assert
        self.assertTrue(res)

    def test_not_same_state(self):
        # Arrange
        sut = Layout.from_file("test/day11/example_input")
        other = Layout.from_file("test/day11/example_round_1")

        # Act
        res = sut.is_same_state(other)

        # Assert
        self.assertFalse(res)

    @parameterized.expand([("example_input", 0), ("example_round_5", 37)])
    def test_occupied_seat_count(self, input_file: str, expected_count: int):
        # Arrange
        test_path = "test/day11/"
        sut = Layout.from_file(test_path + input_file)

        # Act
        count = sut.occupied_seat_count()

        # Assert
        self.assertEqual(count, expected_count)

    @parameterized.expand([("example_input", "example_round_1")])
    def test_simulate_round(self, input_file: str, expected_result_file: str):
        # Arrange
        test_path = "test/day11/"
        sut = Layout.from_file(test_path + input_file)
        expected = Layout.from_file(test_path + expected_result_file)

        # Act
        end = sut.simulate_round()

        # Assert
        self.assertTrue(end.is_same_state(expected))
