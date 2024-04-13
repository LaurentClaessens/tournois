import math

from src.player import Player


class Fight:
    def __init__(self, winner: Player, loser: Player):
        self.winner = winner
        self.loser = loser

    def probability(self):
        """The probability that the winner actually won."""
        mean = self.winner.mean - self.loser.mean
        sigma = math.sqrt(self.winner.sigma**2+self.loser.sigma**2)
        return 1-normal(-mean/sigma)


def normal(x: float) -> float:
    """The normal distribution"""
    return (1/math.sqrt(2*math.pi))*math.exp(-x**2/2)
