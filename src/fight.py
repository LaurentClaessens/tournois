import math

from scipy.stats import norm
from src.player import Player


class Fight:
    def __init__(self, winner: Player, loser: Player):
        self.winner = winner
        self.loser = loser

    def probability(self):
        """The probability that the winner actually won."""
        mean = self.winner.mean - self.loser.mean
        sigma = math.sqrt(self.winner.sigma**2+self.loser.sigma**2)
        f_proba = 1 - norm.cdf(0, mean, sigma)
        return f_proba

    def simul_proba(self, N: int = 50000):
        """Compute the probability by simulating."""
        success: list[bool] = []
        for _ in range(0, N):
            s1 = self.winner.get_strength()
            s2 = self.loser.get_strength()
            success.append(s1 > s2)
        return sum(success)/len(success)


def normal(x: float) -> float:
    """The normal distribution"""
    return (1/math.sqrt(2*math.pi))*math.exp(-x**2/2)
