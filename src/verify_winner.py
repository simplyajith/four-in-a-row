class BoardWinner:
	"""
	This class will contain all the private methods to verify if a game is won or drawn.
	"""
	
	@staticmethod
	def __verify_all_consecutive_columns_are_same(board, row_val, player_symbol):
		"""
		
		:param board: game board, player is playing
		:param row_val: current row, player played
		:param player_symbol: symbol of the current player
		:return: True if 4 consecutive column in the row played by the user are same
				False, otherwise
		"""
		
		col_val = 0
		while col_val < len(board[0]) - 3:
			
			if board[row_val][col_val] == player_symbol and board[row_val][col_val + 1] == player_symbol and \
					board[row_val][col_val + 2] == player_symbol and board[row_val][col_val + 3] == player_symbol:
				return True
			col_val += 1
		
		return False
	
	@staticmethod
	def __verify_all_consecutive_rows_are_same(board, column, player_symbol):
		"""
		
		:param board: game board, player is playing
		:param column: current column played by the player
		:param player_symbol: symbol of the current player
		:return: True if 4 consecutive row in the column played by the user are same
				False, otherwise
		"""
		
		row = 0
		while row < len(board) - 3:
			
			if board[row][column] == player_symbol and board[row + 1][column] == player_symbol and board[row + 2][
				column] == player_symbol and board[row + 3][column] == player_symbol:
				return True
			row += 1
		return False
	
	@staticmethod
	def __verify_all_diagonals_are_same(board, player_symbol):
		"""
		
		:param board: game board, player is playing
		:param player_symbol: symbol of the current player
		:return: True, if 4 consecutive diagonal elements starting from top left to bottom right,having the same
				 symbol of current player
				False,otherwise
		"""
		
		row = 0
		while row < len(board) - 3:
			column = 0
			while column < len(board[0]) - 3:
				# print((row,column),(row+1,column+1),(row+2,column+2),(row+3,column+3))
				if board[row][column] == player_symbol and board[row + 1][column + 1] == player_symbol and \
						board[row + 2][column + 2] == player_symbol and board[row + 3][column + 3] == player_symbol:
					return True
				column += 1
			row += 1
		
		return False
	
	@staticmethod
	def __verify_all_diagonals_are_same_from_bottom(board, player_symbol):
		"""
		
		:param board: game board, player is playing
		:param player_symbol:  symbol of the current player
		:return: True, if 4 consecutive diagonal elements starting from bottom left to top right,having the same
				 symbol of current player
				False,otherwise
		"""
		
		row = len(board) - 1
		while row >= 3:
			column = 0
			while column < len(board[0]) - 3:
				# print((row, column), (row - 1, column + 1), (row - 2, column + 2), (row - 3, column + 3))
				if board[row][column] == player_symbol and board[row - 1][column + 1] == player_symbol and \
						board[row - 2][column + 2] == player_symbol and board[row - 3][column + 3] == player_symbol:
					return True
				column += 1
			row -= 1
		return False
	
	def verify_winner(self, board, row_val, col_val, player_symbol):
		"""
		
		:param board: game board, player is playing
		:param row_val: current row, player played
		:param col_val: current column played by the player
		:param player_symbol: symbol of the current player
		:return: True, if any of row or column or diagonal verification methods returns True
				False, otherwise
		"""
		
		all_columns = self.__verify_all_consecutive_columns_are_same(board, row_val, player_symbol)
		all_rows = self.__verify_all_consecutive_rows_are_same(board, col_val, player_symbol)
		all_diagonals = self.__verify_all_diagonals_are_same(board, player_symbol) or \
						self.__verify_all_diagonals_are_same_from_bottom(board, player_symbol)
		return all_columns or all_rows or all_diagonals
	
	def verify_drawn(self, board):
		"""
		
		:param board: game board, player is playing
		:return: True, if top row of the board is not zero
				False, otherwise
		"""
		
		for i in range(len(board[0])):
			if board[0][i] == 0:
				return False
		return True
