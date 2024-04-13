#!venv/bin/python3

import random

from src.poule import Poule
from src.player import Player


def create_players() -> list[Player]:
    players = []
    for num in range(1, 5):
        name = f"player_{num}"
        mean = num
        sigma = random.uniform(0, 2)
        player = Player(name, mean, sigma)
        players.append(player)
    return players


players = create_players()
real_poule = Poule(players)
print("proba de la poule:", real_poule.probability())
