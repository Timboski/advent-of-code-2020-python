import unittest

from advent2020.day3.puzzle_map import PuzzleMap


class TestPuzzleMap(unittest.TestCase):
    def test_read_example_map(self):
        # Arrange
        example_input = "test/day3/example_input"

        # Act
        map = PuzzleMap(example_input)

        # Assert
        self.assertEqual(map.y_size, 11)
        # First row: ..##.......
        self.assertFalse(map.is_tree(0, 0))
        self.assertFalse(map.is_tree(1, 0))
        self.assertTrue(map.is_tree(2, 0))
        self.assertTrue(map.is_tree(3, 0))
        self.assertFalse(map.is_tree(9, 0))
        self.assertFalse(map.is_tree(10, 0))
        # With overlap
        self.assertFalse(map.is_tree(12, 0))
        self.assertTrue(map.is_tree(13, 0))
        # Last row: .#..#...#.#
        self.assertFalse(map.is_tree(0, 10))
        self.assertTrue(map.is_tree(1, 10))
        self.assertFalse(map.is_tree(5, 10))
        self.assertFalse(map.is_tree(9, 10))
        self.assertTrue(map.is_tree(10, 10))
        # With overlap
        self.assertTrue(map.is_tree(12, 10))
        # Middle
        self.assertTrue(map.is_tree(4, 3))
        self.assertFalse(map.is_tree(3, 5))
