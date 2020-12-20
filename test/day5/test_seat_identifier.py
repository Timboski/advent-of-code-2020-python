import unittest
from parameterized import parameterized

from advent2020.day5.seat_identifier import SeatIdentifier


class TestSeatIdentifier(unittest.TestCase):
    '''
    BFFFBBFRRR: row 70, column 7, seat ID 567.
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    BBFFBBFRLL: row 102, column 4, seat ID 820.
    '''
    @parameterized.expand([("BFFFBBFRRR", 70), ("FFFBBBFRRR", 14),
                           ("BBFFBBFRLL", 102)])
    def test_seat_identifier_return_expected_row(self, seat_id: str, expected_row: int):
        # Arrange, Act
        sut = SeatIdentifier(seat_id)

        # Assert
        self.assertEqual(sut.row, expected_row)
