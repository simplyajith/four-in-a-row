from src.game_board import Player,Board




def play(p1,p2):
	"""
	Function used to initiate the Game.
	Play will be quit if the game is drawn or if a player has won the game.
	:return: None
	"""
	
	g1 = Board(7, 7, p1, p2)
	
	if g1.choose_start():
		while not g1.get_player():
			g1.print_board()
		g1.print_board()
	else:
		play(p1,p2)


if __name__ == "__main__":
	player1_name = input("Enter player1 name: ")
	player2_name = input("Enter player2 name: ")
	p1 = Player(player1_name)
	p2 = Player(player2_name)
	play(p1,p2)
