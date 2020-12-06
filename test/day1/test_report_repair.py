import unittest

from advent2020.day1.report_repair import ReportRepair


class TestReportRepair(unittest.TestCase):
    def test_example_data_should_give_same_result(self):
        # Arrange
        input_data = [1721, 979, 366, 299, 675, 1456]
        sut = ReportRepair()

        # Act
        result = sut.parse(input_data)

        # Assert
        self.assertEqual(result, 514579)
