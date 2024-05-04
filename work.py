#!venv/bin/python3


from src.player import Player
from src.fight import Fight

player1 = Player("player_1", 2, 1)
player2 = Player("player_2", 1, 1)

fight = Fight(player1, player2)
print(fight.simul_proba())
print(fight.probability())
diff = fight.simul_proba() - fight.probability()
print(diff)
