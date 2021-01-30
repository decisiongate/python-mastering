from dataclasses import dataclass, field
from typing import List, Iterable

from python_mastering.decision import Decision


@dataclass
class Insight:
    database: str
    dataset: str
    decisions: List[Decision] = field(default_factory=list)

    def add_decision(self, decision: Decision):
        self.decisions.append(decision)

    def add_decisions(self, decisions: Iterable[Decision]):
        self.decisions.extend(decisions)

    @property
    def primary_decision(self):
        return self.decisions[0]
