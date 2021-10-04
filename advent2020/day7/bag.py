from __future__ import annotations

from typing import Dict, Set


class Bag:
    def __init__(self, rule: str) -> None:
        self.colour, rules = rule.split(" bags contain ")
        self.contents = Bag._process_bag(rules)

    def contains(self, colour: str, bags: Dict[str, Bag]) -> bool:
        if any([c == colour for c in self.contents]):
            return True
        return any([bags[c].contains(colour, bags) for c in self.contents])

    @staticmethod
    def _process_bag(rules: str) -> Set[str]:
        if "no other " in rules:
            return set()
        return {Bag._process_rule(r) for r in rules.split(",")}

    @staticmethod
    def _process_rule(rule: str) -> str:
        sections = rule.strip().split(" ")
        return " ".join(sections[1:-1])
