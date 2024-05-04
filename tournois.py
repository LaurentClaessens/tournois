#!venv/bin/python3


from src.team import Team
from src.poule import Poule
from src.player import Player
from src.fight import Fight
from src.tournament_result import TournamentResult
from src.find_min import Point
from src.find_min import find_min


player_names: list[str] = [f"player_{num}" for num in range(1, 5)]


def create_team() -> Team:
    players = []
    for num in range(0, len(player_names)):
        name = player_names[num]
        mean = num * 10
        sigma = 0.1
        player = Player(name, mean, sigma)
        players.append(player)
    return Team(players)


def result_proba(results: TournamentResult, team: Team) -> float:
    """Say the probability of the results for that team."""
    proba = 1

    for fr in results:
        winner = team.get_player(fr.winner_name)
        loser = team.get_player(fr.loser_name)
        fight = Fight(winner, loser)
        proba *= fight.simul_proba()
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
        return result_proba(self.results, team)


real_team = create_team()
real_poule = Poule(real_team)
real_results = real_poule.results()
print("proba de la poule:", real_poule.probability())
print(real_results)
print(result_proba(real_results, real_team))

to_minimize = ToMinimize(real_results)

x0 = Point([4, 0, 3, 0, 2, 0, 1, 0])
print("----- go pour opti")
x_min = find_min(to_minimize, x0)
print("----- fin de opti")

team = point_to_team(x_min)
proba = result_proba(real_results, team)
print("---- équipe opti")
print(team)
print("-----")
print(f"la proba des résultats avec cette équippe: {proba}")
