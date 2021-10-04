import unittest

from advent2020.day7.bag import Bag


class TestBag(unittest.TestCase):
    def test_construction_from_rule_definition(self):
        # Arrange
        rule = "light red bags contain 1 bright white bag, 2 muted yellow bags."
        expected_contents = {"bright white", "muted yellow"}

        # Act
        sut = Bag(rule)

        # Assert
        self.assertEqual(sut.colour, "light red")
        self.assertSetEqual(sut.contents, expected_contents)
