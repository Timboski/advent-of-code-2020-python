import unittest

from advent2020.day10.adapter_array import AdapterArray


class TestAdapterArray(unittest.TestCase):
    def test_example_input_1(self):
        # Arrange
        path = "test/day10/example_input_1"
        sut = AdapterArray(path)

        # Act
        num = sut.find_sum()

        # Assert
        self.assertEqual(num, 7)

    def test_example_input_2(self):
        # Arrange
        path = "test/day10/example_input_2"
        sut = AdapterArray(path)

        # Act
        num = sut.find_sum()

        # Assert
        self.assertEqual(num, 220)
