#!venv/bin/python3

import math


import dirmanage
from src.team import Team
from src.poule import Poule
from src.player import Player
from src.fight import Fight
from src.tournament_result import TournamentResult
from src.find_min import Point
from src.find_min import find_min
from src.utilities import dprint
from src.utilities import read_json_file


player_names: list[str] = [f"player_{num}" for num in range(1, 5)]


def simulate_poule(team: Team):
    """Simultate fights from the team."""
    fights: list[Fight] = []
    players = team.players
    for num, player1 in enumerate(players):
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


def create_poule(team: Team, data: dict) -> Poule:
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
    poule = Poule(team)
    poule.fights = fights
    return poule


def create_team(data: dict) -> Team:
    players: set[Player] = set()
    for name in data["names"]:
        players.add(Player(name, 0, 0.1))
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


def point_to_team(x: Point):
    """Create a team with the given properties."""
    players: list[Player] = []
    for num, name in enumerate(player_names):
        mean = x[2*num]
        sigma = x[2*num+1]
        player = Player(name, mean, sigma)
        players.append(player)
    team = Team(players)
    return team


class ToMinimize:
    """Probability of getting the result with the given parameters."""

    def __init__(self, results: TournamentResult):
        self.results = results

    def __call__(self, x: Point) -> float:
        team = point_to_team(x)
        proba = result_proba(self.results, team)
        dprint("la proba que je devrais maximiser:", proba)
        if proba == 0:
            return 100
        ans = -math.log(proba)
        print("après log", ans)
        return ans


data_file = dirmanage.init_dir / "bcf.json"
data = read_json_file(data_file)
real_team = create_team(data_file)
real_poule = create_poule(team, data_file)
real_results = real_poule.results()
to_minimize = ToMinimize(real_results)

x0 = Point([3, 0, 3, 0, 3, 0, 3, 0])
team0 = point_to_team(x0)
x_min = find_min(to_minimize, x0)

team = point_to_team(x_min)
proba = result_proba(real_results, team)
print("-----")
print("Équippe réelle")
print(real_team)
print("---- équipe opti")
print(team)
print("-----")
print(f"la proba des résultats avec cette équippe: {proba}")
