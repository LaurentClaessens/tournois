class Player:

    def __init__(self, name: str, mean: float, sigma: float):
        # The strength of this player follows
        # N(mean, v^2)
        self.name = name
        self.mean = mean
        self.sigma = sigma
