import unittest

from advent2020.day11.layout import Layout
from parameterized import parameterized


class TestLayout(unittest.TestCase):
    @parameterized.expand([("example_input", "example_round_1")])
    def test_simulate_round(self, input_file: str, expected_result_file: str):
        # Arrange
        test_path = "test/day11/"
        sut = Layout(test_path + input_file)
        expected = Layout(test_path + expected_result_file)

        # Act
        end = sut.simulate_round()

        # Assert
        self.assertTrue(end.is_same_state(expected))
