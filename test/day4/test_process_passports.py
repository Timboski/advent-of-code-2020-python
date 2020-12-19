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
