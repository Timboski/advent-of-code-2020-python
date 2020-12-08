import unittest

from advent2020.day2.password_entry import PasswordEntry
from parameterized import parameterized


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

    @parameterized.expand([("1-3 a: abcde",), ("1-3 b: cdefg",), ("2-9 c: ccccccccc",)])
    def test_decompose_examples(self, entry: str):
        # Arrange, Act
        sut = PasswordEntry(entry)

        # Assert
        rebuild = f"{sut.min}-{sut.max} {sut.letter}: {sut.password}"
        self.assertEqual(rebuild, entry)
