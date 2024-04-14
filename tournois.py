#!venv/bin/python3

import random

from src.team import Team
from src.poule import Poule
from src.player import Player
from src.fight import Fight
from src.stubs import FightResult


def create_team() -> Team:
    players = []
    for num in range(1, 5):
        name = f"player_{num}"
        mean = num
        sigma = random.uniform(0, 2)
        player = Player(name, mean, sigma)
        players.append(player)
    return Team(players)


def result_proba(results: list[FightResult], team: Team) -> float:
    """Say the probability of the results for that team."""
    proba = 1
    for fr in results:
        winner = team.get_player(fr.winner_name)
        loser = team.get_player(fr.loser_name)
        fight = Fight(winner, loser)
        proba *= fight.probability()
    return proba


team = create_team()
real_poule = Poule(team)
real_results = real_poule.results()
print("proba de la poule:", real_poule.probability())
print(real_results)
