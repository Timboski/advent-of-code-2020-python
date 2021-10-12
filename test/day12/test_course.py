import unittest

from advent2020.day12.course import Course
from parameterized import parameterized


class TestCourse(unittest.TestCase):
    @parameterized.expand([
        ("Example", "test/day12/example_input", 25),
        ("Example", "advent2020/day12/input", 2847),
    ])
    def test_puzzle_1(self, test_name: str, path: str, expected_result: int):
        # Arrange
        sut = Course(path)

        # Act
        dist = sut.find_distance()

        # Assert
        self.assertEqual(dist, expected_result)

    @parameterized.expand([
        ("Example", "test/day12/example_input", 286),
        ("Example", "advent2020/day12/input", 29839),
    ])
    def test_puzzle_2(self, test_name: str, path: str, expected_result: int):
        # Arrange
        sut = Course(path)

        # Act
        dist = sut.find_distance_using_waypoint()

        # Assert
        self.assertEqual(dist, expected_result)
