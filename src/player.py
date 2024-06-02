import numpy


class Player:

    def __init__(self, name: str, mean: float, sigma: float):
        # The strength of this player follows
        # N(mean, v^2)
        self.name = name
        self.mean = mean
        self.sigma = sigma

    def get_strength(self) -> float:
        """Return the instant strength of the player."""
        if self.sigma <= 0:
            # The optimizer has no idea of what sigma is.
            # It could get a negative value
            return self.mean
        return numpy.random.normal(self.mean, self.sigma, 1)[0]

    def __repr__(self):
        return f"{self.name}(mean={self.mean}, sigma={self.sigma})"
