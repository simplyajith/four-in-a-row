from src.verify_winner import BoardWinner
from pytest import mark


class TestBoardWinner:
	win_obj = BoardWinner()
	
	@mark.smoke
	def test_increase_cols(self):
		
		"""
		:return:Initates a (7,7) board to verify consecutive one in the columns
		"""
		
		board = [[0 for _ in range(7)] for _ in range(7)]
		
		start, end = 0, 4
		row = 0
		symbol = "X"
		
		while row < 7:
			while end < 8:
				
				for i in range(start, end):
					board[row][i] = symbol
				
				# Displaying rows for tester reference
				for j in board:
					print(*j, sep = "   ")
				
				print()
				
				actual = self.win_obj.verify_winner(board, row, 0,symbol)
				assert actual == True
				
				board = [[0 for _ in range(7)] for _ in range(7)]
				
				start += 1
				end += 1
			start, end = 0, 4
			row += 1
	
	@mark.smoke
	def test_increase_cols_fail(self):
		"""
		Only three columns are having consecutive symbols, so the tests should fail
		:return: Boolean
		"""
		
		board = [[0 for _ in range(7)] for _ in range(7)]
		
		start, end = 0, 4
		row = 0
		symbol = "X"
		
		while row < 6:
			while end < 8:
				
				for i in range(start, end - 1):
					board[row][i] = symbol
				
				# Displaying rows in console for debugging
				for j in board:
					print(*j)
				
				print()
				actual = self.win_obj.verify_winner(board, row,0, symbol)
				assert actual == False
				
				board = [[0 for _ in range(7)] for _ in range(7)]
				
				start += 1
				end += 1
			start, end = 0, 4
			row += 1
	
	@mark.smoke
	def test_decrease_consecutives_fail(self):
		"""
		:return: False for three consecutive ones and True after adding a one in the consecutive column
		"""
		board = [[0 for _ in range(7)] for _ in range(7)]
		
		start = 6
		symbol = 1
		
		for i in range(start,start-3,-1):

			board[0][i] = symbol
			actual = self.win_obj.verify_winner(board, 0, 0,symbol)
			assert actual == False
		
		board[0][3] = symbol

		actual = self.win_obj.verify_winner(board, 0,0, symbol)
		assert actual == True
			
	
	@mark.smoke
	def test_consecutive_rows(self):
		"""
		
		:return:
		"""
		
		board = [[0 for _ in range(7)] for _ in range(7)]
		
		start, end = 0, 4
		column = 0
		symbol = "X"
		
		while column < 7:
			while end < 8:
				
				
				for i in range(start, end):
					board[i][column] = symbol
				
				# Displaying rows in console for debugging
				print()
				for j in board:
					print(*j)
				print()
				
				actual = self.win_obj.verify_winner(board, 0, column, symbol)
				assert actual == True
				
				board = [[0 for _ in range(7)] for _ in range(7)]
				
				start += 1
				end += 1
			start, end = 0, 4
			column += 1
	
	@mark.smoke
	def test_consecutive_diagonals_from_top_left(self):
		
		board = [[0 for _ in range(7)] for _ in range(7)]
		row = 0
		symbol = "X"
		while row < len(board)-3:
			column = 0
			while column < len(board[0])-3:

				for i in range(0,4):
					board[row+i][column+i] = symbol
					
				# Displaying rows in console for debugging
				print()
				for j in board:
					print(*j)
				print()
				
				actual = self.win_obj.verify_winner(board, row, column, symbol)
				assert actual == True
				
				column += 1
			row += 1
	
	@mark.smoke
	def test_consecutive_diagonals_from_bottom_left(self):
		
		board = [[0 for _ in range(6)] for _ in range(7)]
		row = len(board)-1
		symbol = "X"
		while row >=3:
			column = 0
			while column < len(board[0]) - 3:
				
				for i in range(0, 4):
					board[row - i][column + i] = symbol
				
				# Displaying rows in console for debugging
				print()
				for j in board:
					print(*j)
				print()
				
				actual = self.win_obj.verify_winner(board, row, column, symbol)
				assert actual == True
				
				column += 1
			row -= 1
	
	@mark.smoke
	def test_verify_drawn_success(self):
		"""
		:return: Sets all the values in the board as 1 and verify,if verify draw function returns True.
		"""
		board = [[1 for _ in range(7)] for _ in range(7)]
		actual = self.win_obj.verify_drawn(board)
		assert actual == True
	
	@mark.smoke
	def test_verify_drawn_failure(self):
		"""

		:return:verify draw function should return False for the input boards
		"""
		board1 = [[0 for _ in range(7)] for _ in range(7)]
		board2= [[1,0,0]]
		boards = [board1,board2]
		for board in boards:
			actual = self.win_obj.verify_drawn(board)
			assert actual == False