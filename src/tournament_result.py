"""The results of a tournament."""

from src.stubs import FightResult


class TournamentResult:
    """A wrapper around a list of results."""

    def __init__(self):
        self.results: list[FightResult] = []

    def append(self, result: FightResult):
        """Add a fight to the tournament."""
        self.results.append(result)

    def __str__(self):
        """Print the results."""
        lines: list[str] = []
        for res in self:
            lines.append(str(res))
        return "\n".join(lines)

    def __getitem__(self, index):
        return self.results[index]
