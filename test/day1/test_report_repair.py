import unittest

from advent2020.day1.report_repair import ReportRepair


class TestReportRepair(unittest.TestCase):
    def test_example_data_should_give_same_result(self):
        # Arrange
        input_data = {1721, 979, 366, 299, 675, 1456}
        sut = ReportRepair()

        # Act
        result = sut.find_2_numbers(input_data)

        # Assert
        self.assertEqual(result, 514579)

    def test_read_file_to_a_set(self):
        # Arrange
        input_data = {1721, 979, 366, 299, 675, 1456}
        input_data_path = "test/day1/example_report"
        sut = ReportRepair()

        # Act
        data = sut.read_report(input_data_path)

        # Assert
        self.assertSequenceEqual(data, input_data)

    def test_find_three_numbers_should_give_example_result(self):
        # Arrange
        input_data = {1721, 979, 366, 299, 675, 1456}
        sut = ReportRepair()

        # Act
        result = sut.find_3_numbers(input_data)

        # Assert
        self.assertEqual(result, 241861950)

    def test_check_puzzle1_solution(self):
        # Arrange
        sut = ReportRepair()
        input_data = sut.read_report("advent2020/day1/input")

        # Act
        result = sut.find_2_numbers(input_data)

        # Assert
        self.assertEqual(result, 633216)

    def test_check_puzzle2_solution(self):
        # Arrange
        sut = ReportRepair()
        input_data = sut.read_report("advent2020/day1/input")

        # Act
        result = sut.find_3_numbers(input_data)

        # Assert
        self.assertEqual(result, 68348924)
