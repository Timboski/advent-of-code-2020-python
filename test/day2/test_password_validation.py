import unittest
from advent2020.day2.password_validation import PasswordValidation


class TestPasswordValidation(unittest.TestCase):
    def test_first_example_is_valid(self):
        # Arrange
        entry = "1-3 a: abcde"
        sut = PasswordValidation()

        # Act
        result = sut.validate(entry)

        # Assert
        self.assertTrue(result)
