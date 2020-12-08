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

    def test_second_example_is_not_valid(self):
        # Arrange
        entry = "1-3 b: cdefg"
        sut = PasswordValidation()

        # Act
        result = sut.validate(entry)

        # Assert
        self.assertFalse(result)

    def test_third_example_is_valid(self):
        # Arrange
        entry = "2-9 c: ccccccccc"
        sut = PasswordValidation()

        # Act
        result = sut.validate(entry)

        # Assert
        self.assertTrue(result)

    def test_read_file_to_a_list(self):
        # Arrange
        example_data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
        example_data_path = "test/day2/example_data"
        sut = PasswordValidation()

        # Act
        data = sut.read_entries_from_file(example_data_path)

        # Assert
        self.assertSequenceEqual(data, example_data)

    def test_count_vaild_entries_in_examaple_data_file(self):
        # Arrange
        example_data_path = "test/day2/example_data"
        sut = PasswordValidation()

        # Act
        count = sut.count_valid_entries_in_file(example_data_path)

        # Assert
        self.assertEqual(count, 2)

    def test_validate_puzzle1_answer(self):
        # Arrange
        example_data_path = "advent2020/day2/input"
        sut = PasswordValidation()

        # Act
        count = sut.count_valid_entries_in_file(example_data_path)

        # Assert
        self.assertEqual(count, 536)
