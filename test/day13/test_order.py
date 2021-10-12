import unittest

from advent2020.day13.order import Order
from parameterized import parameterized


class TestOrder(unittest.TestCase):
    @parameterized.expand([
        ("Example1", "17,x,13,19", 3417),
        ("Example2", "67,7,59,61", 754018),
        ("Example3", "67,x,7,59,61", 779210),
        ("Example4", "67,7,x,59,61", 1261476),
        ("Example5", "1789,37,47,1889", 1202161486),
    ])
    def test_puzzle_1(self, test_name: str, busses: str, expected_result: int):
        # Arrange
        sut = Order(busses)

        # Act
        ans = sut.find_sequence_start_time()

        # Assert
        self.assertEqual(ans, expected_result)
