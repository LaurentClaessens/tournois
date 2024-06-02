"""Represent a list of players."""

import random

from src.player import Player
from src.utilities import dprint
_ = dprint


class Team:

    def __init__(self, players: list[Player]):
        self.players = players

    def get_player(self, name: str) -> Player:
        """Return the player with requested name."""
        for player in self.players:
            if player.name == name:
                return player
        raise NameError(f"No player with that name: {name}")

    def simulate_points(self):
        """Simulate random fights and count the points."""
        play_to_points = {player: 0 for player in self.players}
        for _ in range(0, 1000):
            play1 = random.choice(self.players)
            play2 = random.choice(self.players)
            if play1 == play2:
                continue
            print(f"{play1.name} Vs {play2.name}")
            s1 = play1.get_strength()
            s2 = play2.get_strength()
            if s1 > s2:
                play_to_points[play1] += 1
            if s1 < s2:
                play_to_points[play2] += 1

        answer = dict(sorted(play_to_points.items(), key=lambda x: x[1]))
        return answer

    def __str__(self):
        """Print the team sorted by mean."""
        lines: list[str] = []
        s_players = list(self.players)
        s_players.sort(key=lambda x: x.mean)
        for player in s_players:
            lines.append(player.name)
            lines.append(f"  {player.mean}")
            lines.append(f"  {player.sigma}")
        return "\n".join(lines)
