from typing import Union
from pathlib import Path

PathOrStr = Union[Path, str]


class FightResult:

    def __init__(self, name1: str, name2: str, winner_name: str):
        self.name1 = name1
        self.name2 = name2
        self.winner_name = winner_name
        self.loser_name = self.get_loser()

    def get_loser(self):
        if self.winner_name == self.name1:
            return self.name2
        if self.winner_name == self.name2:
            return self.name1
        raise NameError("Incohérence")

    def __str__(self):
        return f"{self.name1} Vs {self.name2} --> {self.winner_name}"
