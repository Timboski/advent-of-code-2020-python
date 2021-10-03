import unittest

from advent2020.day6.customs_declarations import CustomsDeclarations


class TestCustomsDeclarations(unittest.TestCase):
    def test_example_input(self):
        # Arrange
        path = "test/day6/example_input"
        sut = CustomsDeclarations(path)

        # Act
        res = sut.yes_count()

        # Assert
        self.assertEqual(res, 11)
