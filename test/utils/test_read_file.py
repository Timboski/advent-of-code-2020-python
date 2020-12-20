import unittest

from advent2020.utils.read_file import ReadFile


class TestPasswordValidation(unittest.TestCase):
    def test_read_lines_from_a_file(self):
        # Arrange
        example_data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
        example_data_path = "test/day2/example_data"

        # Act
        data = ReadFile.lines(example_data_path)

        # Assert
        self.assertSequenceEqual(data, example_data)
