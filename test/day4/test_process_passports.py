import unittest

from advent2020.day4.process_passports import ProcessPassports


class TestProcessPassports(unittest.TestCase):
    def test_read_4_passports_from_example_data(self):
        # Arrange
        passport_file_path = "test/day4/example_passports"

        # Act
        sut = ProcessPassports(passport_file_path)

        # Assert
        self.assertEqual(sut.num_passports, 4)

    def test_validate_2_passports_from_example_data(self):
        # Arrange
        passport_file_path = "test/day4/example_passports"
        sut = ProcessPassports(passport_file_path, validate_contents=False)

        # Act
        valid = sut.validate_passports()

        # Assert
        self.assertEqual(valid, 2)

    def test_validate_puzzle1_answer(self):
        # Arrange
        input = "advent2020/day4/input"
        sut = ProcessPassports(input, validate_contents=False)

        # Act
        valid = sut.validate_passports()

        # Assert
        self.assertEqual(valid, 264)

    def test_invalid_passport_contents(self):
        # Arrange
        passport_file_path = "test/day4/invalid_passports"
        sut = ProcessPassports(passport_file_path)

        # Act
        valid = sut.validate_passports()

        # Assert
        self.assertEqual(valid, 0)

    def test_valid_passport_contents(self):
        # Arrange
        passport_file_path = "test/day4/valid_passports"
        sut = ProcessPassports(passport_file_path)

        # Act
        valid = sut.validate_passports()

        # Assert
        self.assertEqual(valid, 4)

    def test_validate_puzzle2_answer(self):
        # Arrange
        input = "advent2020/day4/input"
        sut = ProcessPassports(input)

        # Act
        valid = sut.validate_passports()

        # Assert
        self.assertEqual(valid, 224)
