import unittest

from advent2020.day7.haversacks import Haversacks


class TestHaversacks(unittest.TestCase):
    def test_example_input(self):
        # Arrange
        path = "test/day7/example_input"
        sut = Haversacks(path)

        # Act
        res = sut.num_colour_options()

        # Assert
        self.assertEqual(res, 4)

    def test_validate_puzzle1_answer(self):
        # Arrange
        path = "advent2020/day7/input"
        sut = Haversacks(path)

        # Act
        res = sut.num_colour_options()

        # Assert
        self.assertEqual(res, 289)
