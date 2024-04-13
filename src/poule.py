import numpy

from src.player import Player
from src.fight import Fight
from src.utilities import dprint
_ = dprint


class Poule:
    """All the fights with the players."""

    def __init__(self, players: list[Player]):
        self.players = players
        self.fights = self.create_fights()

    def create_fights(self) -> list[Fight]:
        fights: list[Fight] = []
        for num, player1 in enumerate(self.players):
            for player2 in self.players[num+1:]:
                print(f"{player1.name} Vs {player2.name}")
                s1 = numpy.random.normal(player1.mean, player1.sigma, 1)[0]
                s2 = numpy.random.normal(player2.mean, player2.sigma, 1)[0]
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
