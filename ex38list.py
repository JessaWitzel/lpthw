#find 10 examples of things in the real world that would fit in a list. Write scripts that work with them.

games_iown = ["Phase 10", "Dominion", "Munchkin", "Settlers of Catan", "Scrabble", "Apples to Apples", "Rummikub"]

gamechoice = raw_input ("Pick a random number and I will tell you which game to play. \n> ")
gamechoice = int(gamechoice) - 1

while len(games_iown) < gamechoice:
	gamechoice = raw_input("Pick a smaller number, you don't own that many games. \n> ")
	gamechoice = int(gamechoice) - 1
	
print games_iown[gamechoice]
	


