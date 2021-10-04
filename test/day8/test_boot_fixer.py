import unittest

from advent2020.day8.boot_fixer import BootFixer


class TestBootFixer(unittest.TestCase):
    def test_example_input(self):
        # Arrange
        path = "test/day8/example_input"
        sut = BootFixer(path)

        # Act
        acc = sut.fix_and_run()

        # Assert
        self.assertEqual(acc, 8)
