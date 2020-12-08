import unittest
from advent2020.day2.password_validation import PasswordValidation


class TestPasswordValidation(unittest.TestCase):
    def test_read_file_to_a_list(self):
        # Arrange
        example_data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
        example_data_path = "test/day2/example_data"
        sut = PasswordValidation()

        # Act
        data = sut.read_entries_from_file(example_data_path)

        # Assert
        self.assertSequenceEqual(data, example_data)
