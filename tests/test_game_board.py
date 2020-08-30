from src.game_board import Board, Player
import mock
import pytest
import builtins


class TestPlayerAttributes:
	
	def setup(self):
		self.player1 = Player("player1")
	
	@pytest.mark.smoke
	def test_get_flag(self):
		assert self.player1.getflag() is None
	
	@pytest.mark.smoke
	def test_set_flag(self):
		self.player1.setflag(True)
		assert self.player1.getflag() is True
	
	@pytest.mark.smoke
	def test_get_name(self):
		assert self.player1.getname == "player1"
		
		
class TestChooseStart:
	
	@pytest.mark.smoke
	def test_choose_start_option_1(self):
		player1 = Player("player1")
		player2 = Player("player2")
		board_obj = Board(7, 7, player1, player2)
		
		with mock.patch.object(builtins, 'input', lambda _: '1'):
			assert board_obj.choose_start() == True and player1.getflag() == True and player2.getflag() is False
	
	@pytest.mark.smoke
	def test_choose_start_option_2(self):
		player1 = Player("player1")
		player2 = Player("player2")
		board_obj = Board(7, 7, player1, player2)
		
		with mock.patch.object(builtins, 'input', lambda _: '2'):
			assert board_obj.choose_start() == True and player2.getflag() == True and player1.getflag() is False
	
	@pytest.mark.smoke
	def test_choose_start_option_invalid(self):
		player1 = Player("player1")
		player2 = Player("player2")
		board_obj = Board(7, 7, player1, player2)
		
		invalid_data = ["3", "sdfasd", "!@#$"]
		for i in invalid_data:
			with mock.patch.object(builtins, 'input', lambda _: i):
				assert board_obj.choose_start() == False and player1.getflag() is None and player2.getflag() is None


class TestGetPlayer:
	
	
	def setup(self):
		self.player1 = Player("player1")
		self.player2 = Player("player2")
		self.board_obj = Board(7, 7, self.player1, self.player2)
		with mock.patch.object(builtins, 'input', lambda _: '1'):
			self.board_obj.choose_start()
	
	@pytest.mark.smoke
	def test_player1_start(self):
		with mock.patch.object(builtins, 'input', lambda _: 1):
			assert self.board_obj.get_player() == False
	
	@pytest.mark.smoke
	def test_player2_start(self):
		with mock.patch.object(builtins, 'input', lambda _: '2'):
			self.board_obj.choose_start()
		
		with mock.patch.object(builtins, 'input', lambda _: 3):
			assert self.board_obj.get_player() == False



