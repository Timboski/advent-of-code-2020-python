import unittest
from typing import Set

from advent2020.day7.bag import Bag
from parameterized import parameterized


class TestBag(unittest.TestCase):
    @parameterized.expand([
        ("light red", "light red bags contain 1 bright white bag, 2 muted yellow bags.",
         {"bright white", "muted yellow"}),
        ("dark orange",
         "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
         {"bright white", "muted yellow"}),
        ("bright white", "bright white bags contain 1 shiny gold bag.", {"shiny gold"}),
        ("muted yellow",
         "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
         {"shiny gold", "faded blue"}),
        ("shiny gold", "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
         {"dark olive", "vibrant plum"}),
        ("dark olive",
         "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
         {"faded blue", "dotted black"}),
        ("vibrant plum",
         "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
         {"faded blue", "dotted black"}),
        ("faded blue", "faded blue bags contain no other bags.", set()),
        ("dotted black", "dotted black bags contain no other bags.", set()),
    ])
    def test_construction_from_rule_definition(self, colour: str, rule: str,
                                               contents: Set[str]):
        # Arrange
        # Act
        sut = Bag(rule)

        # Assert
        self.assertEqual(sut.colour, colour)
        self.assertSetEqual(set(sut.contents), contents)
