class BoardManager:
	

	@staticmethod
	def verify_columnn_is_valid(board,column):
		"""

		:param column: column chosen by the player to drop players symbol
		:return: True if the top of the column is equal to 0
				False, otherwise
		"""
		
		return board[0][column] == 0
	
	@staticmethod
	def get_valid_row(board,column):
		"""
		:param column: current valid column chosen by the player
		:return: After player, chooses a valid column returns the row value with 0 from the bottom
		"""
		
		row = len(board)
		
		for i in range(row - 1, -1, -1):
			if board[i][column] == 0:
				return i
			
	@staticmethod
	def print_board_common(board):
		"""
		prints the board after every move for players reference.
		:return: None
		"""
		
		column = len(board[0])
		
		for row in [[i for i in range(column)]]:
			print(*row, sep="   ")
		
		print("#" * column * 4)
		
		for row in board:
			print(*row, sep="   ")