class BoardManager:
	
	def __init__(self,board):
		self.board = board
	
	def verify_columnn_is_valid(self,column):
		"""

		:param column: column chosen by the player to drop players symbol
		:return: True if the top of the column is equal to 0
				False, otherwise
		"""
		
		return self.board[0][column] == 0
	
	def get_valid_row(self,column):
		"""
		:param column: current valid column chosen by the player
		:return: After player, chooses a valid column returns the row value with 0 from the bottom
		"""
		
		board = self.board
		row = len(self.board)
		
		for i in range(row - 1, -1, -1):
			if board[i][column] == 0:
				return i
	
	def print_board(self):
		"""
		prints the board after every move for players reference.
		:return: None
		"""
		
		column = len(self.board[0])
		
		for row in [[i for i in range(column)]]:
			print(*row, sep="   ")
		
		print("#" * column * 4)
		
		for row in self.board:
			print(*row, sep="   ")