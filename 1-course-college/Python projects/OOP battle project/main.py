from real_classes import Fighter #Import class from file
from real_classes import Contest

player1 = Fighter("Ned", 100, 10, 5)
player2 = Fighter("Jamy", 100, 10, 5)

battle = Contest()

battle.meet_fighters(player1, player2)

battle.start_battle(player1, player2)

