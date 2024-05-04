import random


from src.fight import Fight
from src.team import Team
from src.tournament_result import TournamentResult
from src.stubs import FightResult
from src.utilities import dprint
_ = dprint


class Poule:
    """All the fights with the players."""

    def __init__(self, team: Team):
        self.players = team.players
        self.fights = self.create_fights()

    def create_fights(self) -> list[Fight]:
        fights: list[Fight] = []
        for num, player1 in enumerate(self.players):
            for player2 in self.players[num+1:]:
                print(f"{player1.name} Vs {player2.name}")
                s1 = player1.get_strength()
                s2 = player2.get_strength()
                if s1 > s2:
                    winner = player1
                    loser = player2
                else:
                    winner = player2
                    loser = player1
                fights.append(Fight(winner, loser))
        return fights

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
