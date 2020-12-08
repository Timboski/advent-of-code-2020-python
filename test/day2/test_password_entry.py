import unittest
from advent2020.day2.password_entry import PasswordEntry


class TestPasswordEntry(unittest.TestCase):
    def test_decompose_first_example(self):
        # Arrange
        entry = "1-3 a: abcde"

        # Act
        sut = PasswordEntry(entry)

        # Assert
        self.assertEqual(sut.min, 1)
        self.assertEqual(sut.max, 3)
        self.assertEqual(sut.letter, "a")
        self.assertEqual(sut.password, "abcde")
