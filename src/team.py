"""Represent a list of players."""

from src.player import Player


class Team:

    def __init__(self, players: set[Player]):
        # The player are a set because I want them
        # to be unordered.
        self.players = players

    def get_player(self, name: str) -> Player:
        """Return the player with requested name."""
        for player in self.players:
            if player.name == name:
                return player
        raise NameError(f"No player with that name: {name}")

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
