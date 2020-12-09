import unittest
from advent2020.day2.puzzle2_validation import Puzzle2Validation


class TestPuzzle1Validation(unittest.TestCase):
    def test_first_example_is_valid(self):
        # Arrange
        entry = "1-3 a: abcde"
        sut = Puzzle2Validation()

        # Act
        result = sut.validate(entry)

        # Assert
        self.assertTrue(result)

    def test_second_example_is_not_valid(self):
        # Arrange
        entry = "1-3 b: cdefg"
        sut = Puzzle2Validation()

        # Act
        result = sut.validate(entry)

        # Assert
        self.assertFalse(result)

    def test_third_example_is_not_valid(self):
        # Arrange
        entry = "2-9 c: ccccccccc"
        sut = Puzzle2Validation()

        # Act
        result = sut.validate(entry)

        # Assert
        self.assertFalse(result)

    def test_count_vaild_entries_in_examaple_data_file(self):
        # Arrange
        example_data_path = "test/day2/example_data"
        sut = Puzzle2Validation()

        # Act
        count = sut.count_valid_entries_in_file(example_data_path)

        # Assert
        self.assertEqual(count, 1)

    def test_validate_puzzle2_answer(self):
        # Arrange
        example_data_path = "advent2020/day2/input"
        sut = Puzzle2Validation()

        # Act
        count = sut.count_valid_entries_in_file(example_data_path)

        # Assert
        self.assertEqual(count, 558)
