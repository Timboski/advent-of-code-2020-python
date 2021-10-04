from __future__ import annotations

from typing import Dict


class Bag:
    def __init__(self, rule: str) -> None:
        self.colour, rules = rule.split(" bags contain ")
        self.contents = Bag._process_bag(rules)

    def contains(self, colour: str, bags: Dict[str, Bag]) -> bool:
        if any([c == colour for c in self.contents]):
            return True
        return any([bags[c].contains(colour, bags) for c in self.contents])

    def num_bags_inside(self, bags: Dict[str, Bag]) -> int:
        return sum([(bags[colour].num_bags_inside(bags) + 1) * self.contents[colour]
                    for colour in self.contents])

    @staticmethod
    def _process_bag(rules: str) -> Dict[str]:
        if "no other " in rules:
            return dict()
        return {c[0]: c[1] for c in [Bag._process_rule(r) for r in rules.split(",")]}

    @staticmethod
    def _process_rule(rule: str) -> str:
        sections = rule.strip().split(" ")
        return " ".join(sections[1:-1]), int(sections[0])
