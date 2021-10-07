import unittest

from advent2020.day9.decoder import Decoder


class TestBoot(unittest.TestCase):
    def test_example_input(self):
        # Arrange
        path = "test/day9/example_input"
        sut = Decoder(path, 5)

        # Act
        num = sut.find_first_invalid()

        # Assert
        self.assertEqual(num, 127)

    def test_validate_puzzle1_answer(self):
        # Arrange
        path = "advent2020/day9/input"
        sut = Decoder(path, 25)

        # Act
        num = sut.find_first_invalid()

        # Assert
        self.assertEqual(num, 26134589)

    def test_example_input_weakness(self):
        # Arrange
        path = "test/day9/example_input"
        sut = Decoder(path, 5)

        # Act
        weakness = sut.find_weakness(127)

        # Assert
        self.assertEqual(weakness, 62)
