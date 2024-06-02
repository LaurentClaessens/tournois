#!venv/bin/python3

import math
import random


import dirmanage
from src.team import Team
from src.tournament import Tournament
from src.player import Player
from src.fight import Fight
from src.tournament_result import TournamentResult
from src.find_min import Point
from src.find_min import find_min
from src.utilities import dprint
from src.utilities import read_json_file


def create_tournament(team: Team, data: dict) -> Tournament:
    """Read the fights in the data."""
    fights: list[Fight] = []
    for level, couples in data["fights"].items():
        print(f"read fights for {level}")
        for couple in couples:
            winner_name = couple[0]
            loser_name = couple[1]
            winner = team.get_player(winner_name)
            loser = team.get_player(loser_name)
            fights.append(Fight(winner, loser))
    tournament = Tournament(team)
    tournament.fights = fights
    return tournament


def create_team(data: dict) -> Team:
    players: list[Player] = []
    for name in data["names"]:
        players.append(Player(name, 0, 0.1))
    return Team(players)


def result_proba(results: TournamentResult, team: Team) -> float:
    """Say the probability of the results for that team."""
    proba = 1

    for fr in results:
        winner = team.get_player(fr.winner_name)
        loser = team.get_player(fr.loser_name)
        fight = Fight(winner, loser)
        proba *= fight.probability()
    return proba


def point_to_team(real_team: Team, x: Point):
    """Create a team with the given properties."""
    real_players = real_team.players
    new_players: list[Player] = []
    for num, player in enumerate(real_players):
        mean = x[2*num]
        sigma = x[2*num+1]
        player = Player(player.name, mean, sigma)
        new_players.append(player)
    team = Team(new_players)
    return team


class ToMinimize:
    """Probability of getting the result with the given parameters."""

    def __init__(self, real_team: Team, results: TournamentResult):
        self.real_team = real_team
        self.results = results

    def __call__(self, x: Point) -> float:
        team = point_to_team(self.real_team, x)
        proba = result_proba(self.results, team)
        dprint("la proba que je devrais maximiser:", proba)
        if proba == 0:
            return 100
        ans = -math.log(proba)
        return ans


def find_one_loc_min(real_team: Team):
    """Create  a random team and optimize it."""
    fl: list[float] = []
    for player in real_team.players:
        mean = random.random()
        sigma = 0.1
        fl.extend([mean, sigma])
    x0 = Point(fl)
    team0 = point_to_team(real_team, x0)
    x_min = find_min(to_minimize, x0)
    return x_min


data_file = dirmanage.init_dir / "bfc.json"
data = read_json_file(data_file)
real_team = create_team(data)
real_tournament = create_tournament(real_team, data)
real_results = real_tournament.results()
to_minimize = ToMinimize(real_team, real_results)


x_min = find_one_loc_min(real_team)
team = point_to_team(real_team, x_min)
proba = result_proba(real_results, team)
print("-----")
print("Équippe réelle")
print(real_team)
print("---- équipe opti")
print(team)
print("-----")
print(f"la proba des résultats avec cette équippe: {proba}")
points = team.simulate_points()
for player, point in points.items():
    print(f"{player.name.ljust(15)} -> {point}")
