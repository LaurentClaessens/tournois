"""Represent a list of players."""

from src.player import Player


class Team:

    def __init__(self, players: list[Player]):
        self.players = players

    def get_player(self, name: str) -> Player:
        """Return the player with requested name."""
        for player in self.players:
            if player.name == name:
                return player
        raise NameError(f"No player with that name: {name}")