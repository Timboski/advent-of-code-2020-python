import unittest

from advent2020.day3.route import Route


class TestRoute(unittest.TestCase):
    def test_example_puzzle(self):
        # Arrange
        example_input = "test/day3/example_input"
        sut = Route(example_input)

        # Act
        trees_encountered = sut.toboggan_run()

        # Assert
        self.assertEqual(trees_encountered, 7)