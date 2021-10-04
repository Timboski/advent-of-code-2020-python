import unittest

from advent2020.day8.boot import Boot


class TestBoot(unittest.TestCase):
    def test_example_input(self):
        # Arrange
        path = "test/day8/example_input"
        sut = Boot(path)

        # Act
        acc = sut.find_acc_at_loop()

        # Assert
        self.assertEqual(acc, 5)
