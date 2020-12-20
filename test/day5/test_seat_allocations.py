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
