import unittest

from advent2020.day5.seat_allocations import SeatAllocations


class TestSeatAllocations(unittest.TestCase):
    def test_find_max_occupied_seat_identifier(self):
        # Arrange
        path = "test/day5/example_input"
        sut = SeatAllocations(path)

        # Act
        max = sut.find_max_occupied()

        # Assert
        self.assertEqual(max, 820)

    def test_validate_puzzle1_answer(self):
        # Arrange
        path = "advent2020/day5/input"
        sut = SeatAllocations(path)

        # Act
        max = sut.find_max_occupied()

        # Assert
        self.assertEqual(max, 888)

    def test_validate_puzzle2_answer(self):
        # Arrange
        path = "advent2020/day5/input"
        sut = SeatAllocations(path)

        # Act
        max = sut.find_empty_seat()

        # Assert
        self.assertEqual(max, 522)
