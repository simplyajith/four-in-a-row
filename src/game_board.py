from src.verify_winner import BoardWinner
from src.board_manger import BoardManager

class Board:
	
	def __init__(self, row, column, player1, player2):
		self.__row = int(row)
		self.__column = int(column)
		self.__board = [[0 for _ in range(self.__column)] for _ in range(self.__row)]
		self.player1 = player1
		self.player2 = player2
		self.__move_symbol = {self.player1: "X", self.player2: "Y"}
		self.win_obj = BoardWinner()
		self.board_manager_obj = BoardManager(self.__board)
		
	def choose_start(self):
		"""
		sets player flag who chooses to start the game
		:return: True if valid input is given
				 False if input is other than "1" or "2"
		"""
		print("#" * 100)
		print("Enter 1 for player 1 to start")
		print("Enter 2 for player 2 to start")
		print("#" * 100)
		choose_player = input("Choose who wants to play the game \n"
							  "1. Player 1. \n"
							  "2. Player 2 \n"
							  "Choice:  ")
		print(choose_player)
		if choose_player == "1":
			self.player1.flag = True
			self.player2.flag = False
			return True
		if choose_player == "2":
			self.player2.flag = True
			self.player1.flag = False
			return True
		else:
			print("Please type input as either 1 or 2")
			return False
	
	def get_player(self):
		"""
		If player1 flag is set as True, player 1 will be allowed to drop his symbol in th board
		Else player 2 will be allowed to drop his symbol.
		:return: True, after player dropped the symbol, if player has won the game or if the the game is drawn.
				False, otherwise.
		
		"""
		if self.player1.flag:
			status = self.__move(self.player1)
			if status:
				return True
		
		else:
			status = self.__move(self.player2)
			if status:
				return True
		
		return False
	
	def print_board(self):
		self.board_manager_obj.print_board()
		
	def __make_move(self, player, column_val):
		
		"""
		1) To drop a symbol, need to validate the column chosen by the player is valid.
		2) If the column, chosen by the player is valid, find the bottom row in the board to place the symbol.
		3) Once the symbol is placed in the board, set played flag as True, to confirm player has dropped the symbol.
		4) After player has dropped the symbol, check for winning conditions and drawn condition.
		5) If player has won or the game is drawn, return True
		6) else, reset flag of the current player to False and set other player flag to True.
		
		:param player: current player playing the game
		:param column_val: column chosen by the current player
		:return: True if the game is drawn or won by the current player
				Else,Resets the flag  of the current player to False
		"""
		
		board = self.__board
		played = False
		
		if self.board_manager_obj.verify_columnn_is_valid(column_val):
			played = True
			valid_row = self.board_manager_obj.get_valid_row(column_val)
			self.__board[valid_row][column_val] = self.__move_symbol[player]
			
			if self.win_obj.verify_winner(board, valid_row, column_val, self.__move_symbol[player]):
				print("*" * 100)
				print(f"Congrats!! {player.name} has won the game.")
				print("*" * 100)
				return True
		
		else:
			
			print(f"The column chosen {column_val} is full.")
			print()
			print("Please enter another column where symbol can be dropped")
			return self.__move(player)
		
		if played:
			
			if self.win_obj.verify_drawn(board):
				print("Thanks for playing the game. The game is drawn")
				return True
			
			self.player1.set_flag(self.player2)
	
	def __move(self, player):
		"""
		once the player enters the column value, checks if it is a valid value.
		Otherwise, requests the user to enter a valid value
		
		:param player: player whose flag is set as True
		:return:True,if the game is won or drawn.
		"""
		
		print(f"Player {player.name}'s turn to drop the symbol")
		print()
		try:
			
			col = int(input(f"Enter the column value between 0 to {self.__column - 1}: "))
			if 0 <= col < self.__column:
				return self.__make_move(player, col)
			else:
				print("Entered value is  invalid")
				return self.__move(player)
		except ValueError as err:
			print("Enter numeric integers for column value")
			return self.__move(player)


class Player:
	"""
	Contains player attributes of the players in the Game
	"""
	
	def __init__(self, name, flag=None):
		self.__name = name
		self.__flag = flag
	
	@property
	def flag(self):
		return self.__flag
	
	@flag.setter
	def flag(self, value):
		self.__flag = value
	
	@property
	def name(self):
		return self.__name
	
	def set_flag(self, other):
		"""
		Resets the player flag to alternate the play between player 1 and 2

		:param player1: player 1
		:param player2: player 2
		:return: If player1 flag is set as True, resets player1 flag as False and sets player2 flag as True
				Else, resets resets player2 flag as False and sets player1 flag as True
		"""
		
		if self.flag:
			self.flag = False
			other.flag = True
		else:
			other.flag = False
			self.flag = True

