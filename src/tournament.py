import random


from src.fight import Fight
from src.team import Team
from src.tournament_result import TournamentResult
from src.stubs import FightResult
from src.utilities import dprint
_ = dprint


class Tournament:
    """All the fights with the players."""

    def __init__(self, team: Team):
        self.players = team.players
        self.fights: list[Fight] = []

    def probability(self) -> float:
        """Say the probability of the results given the players."""
        proba = 1
        for fight in self.fights:
            proba *= fight.probability()
        return proba

    def results(self):
        """Return the raw results."""
        results = TournamentResult()
        for fight in self.fights:
            names = [fight.winner.name, fight.loser.name]
            random.shuffle(names)
            data = {"name1": names[0],
                    "name2": names[1],
                    "winner_name": fight.winner.name}
            results.append(FightResult(**data))
        return results
