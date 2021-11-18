# based on code from https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python
from section2 import Game_Parameter
import time
import string


class Game:
	MINIMAX = 0
	ALPHABETA = 1
	HUMAN = 2
	AI = 3
	current_state = []
	gp = Game_Parameter()
	d1 = gp.max_depth_d1
	d2 = gp.max_depth_d2
	# current_depth_max = 0 #the current depth of the recursion
	# current_depth_min = 0
	nb_of_evaluated_states = 0
	current_depth = 0
	
	def __init__(self, recommend = True):
		self.initialize_game()
		self.recommend = recommend
		#return (int(column_selected), row_selected)

	def mode_of_play(self):
		if self.gp.play_modes.lower() == "h-h":
			return [2, 2]
		elif self.gp.play_modes.lower() == "ai-ai":
			return [3, 3]
		elif self.gp.play_modes.lower() == "h-ai":
			return [2, 3]
		elif self.gp.play_modes.lower() == "ai-h":
			return [3, 2]

	# Takes in board size and blocs
	def initialize_game(self):
		self.player_turn = 'X'
		for i in range(self.gp.size_of_board):
			row = []
			for j in range(self.gp.size_of_board):
				row.append('.')
			self.current_state.append(row)
		for k, z, in enumerate(self.gp.blocs_coordinates):
			x = z[0]
			y = z[1]
			self.current_state[x][y] = '*'

	# no need for modification
	def switch_player(self):
		if self.player_turn == 'X':
			self.player_turn = 'O'
		elif self.player_turn == 'O':
			self.player_turn = 'X'
		return self.player_turn

	def draw_board(self):
		formatted_list = ' '
		for i in range(self.gp.size_of_board):
			formatted_list += ' ' + string.ascii_uppercase[i]
		row_index = 0
		for i in self.current_state:
			formatted_list += '\n' + str(row_index) + '|'
			col_index = 0
			row_index += 1
			for j in i:
				formatted_list += j + ' '
				col_index += 1
		return formatted_list

	def is_end(self):
		horizontal_X_flag = horizontal_O_flag = vertical_X_flag = vertical_O_flag = 0
		# Vertical win
		for i in range(self.gp.size_of_board):
			for j in range(self.gp.size_of_board):
				if (i <= self.gp.size_of_board - self.gp.line_up_size):
					for k in range(self.gp.line_up_size):
						if (self.current_state[i+k][j] == 'X'):
							vertical_X_flag += 1
						elif (self.current_state[i+k][j] == 'O'):
							vertical_O_flag += 1
					if (self.gp.line_up_size == vertical_X_flag):
						return 'X'
					elif (self.gp.line_up_size == vertical_O_flag):
						return 'O'
					vertical_X_flag = vertical_O_flag = 0

		# Horizontal win
		for i in range(self.gp.size_of_board):
			for j in range(self.gp.size_of_board):
				if (j <= self.gp.size_of_board - self.gp.line_up_size):
					for k in range(self.gp.line_up_size):
						if (self.current_state[i][j+k] == 'X'):
							horizontal_X_flag += 1
						elif (self.current_state[i][j+k] == 'O'):
							horizontal_O_flag += 1
					if (self.gp.line_up_size == horizontal_X_flag):
						return 'X'
					elif (self.gp.line_up_size == horizontal_O_flag):
						return 'O'
					horizontal_X_flag = horizontal_O_flag = 0

		# Diagonal win
		diagonal_X_flag = diagonal_O_flag = diagonal_1_X_flag = diagonal_1_O_flag = 0
		for i in range(self.gp.size_of_board):
			for j in range(self.gp.size_of_board):
				if (i <= self.gp.size_of_board - self.gp.line_up_size and j <= self.gp.size_of_board - self.gp.line_up_size):
					for k in range(self.gp.line_up_size):
						if (self.current_state[i + k][j + k] == 'X'):
							diagonal_X_flag += 1
						elif (self.current_state[i + k][j + k] == 'O'):
							diagonal_O_flag += 1
					if diagonal_X_flag == self.gp.line_up_size:
						return 'X'
					elif diagonal_O_flag == self.gp.line_up_size:
						return 'O'
					diagonal_X_flag = diagonal_O_flag = 0

				if (i <= self.gp.size_of_board - self.gp.line_up_size and j >= self.gp.line_up_size - 1):
					for k in range(self.gp.line_up_size):
						if (self.current_state[i + k][j - k] == 'X'):
							diagonal_1_X_flag += 1
						elif (self.current_state[i + k][j - k] == 'O'):
							diagonal_1_O_flag += 1
					if diagonal_1_X_flag == self.gp.line_up_size:
						return 'X'
					elif diagonal_1_O_flag == self.gp.line_up_size:
						return 'O'
					diagonal_1_X_flag = diagonal_1_O_flag = 0

		# Is whole board full?
		for i in range(self.gp.size_of_board):
			for j in range(self.gp.size_of_board):
				# There's an empty field, we continue the game
				if (self.current_state[i][j] == '.'):
					return None
		# It's a tie!
		return '.'

	def check_end(self):
		self.result = self.is_end()
		# Printing the appropriate message if the game has ended
		if self.result != None:
			if self.result == 'X':
				print('The winner is X!')
			elif self.result == 'O':
				print('The winner is O!')
			elif self.result == '.':
				print("It's a tie!")
			self.initialize_game()
		return self.result

	def input_move(self):
		list_of_chars = [string.ascii_uppercase[i] for i in range(self.gp.size_of_board)]
		column_selected = input(
			"Please indicate the column [A-" + string.ascii_uppercase[self.gp.size_of_board - 1] + "]:\n")
		while column_selected not in list_of_chars:
			print("Invalid input")
			column_selected = input(
				"Please indicate the column [A-" + string.ascii_uppercase[self.gp.size_of_board - 1] + "]:\n")
		for i in range(len(list_of_chars)):
			if column_selected == list_of_chars[i]:
				column_selected = str(i)

		row_selected = int(input("Please indicate the row [0-" + str(self.gp.size_of_board - 1) + "]:\n"))
		while row_selected not in [i for i in range(self.gp.size_of_board)]:
			print("Invalid input")
			row_selected = int(input("Please indicate the row [0-" + str(self.gp.size_of_board - 1) + "]:\n"))

		return (int(column_selected), row_selected)

	#Reference the slides in 4.1a
	def possible_win_paths(self):
		score = 0
		horizontal_X_flag = horizontal_O_flag = horizontal_X_score = horizontal_O_score = 0
		vertical_X_flag = vertical_O_flag = vertical_X_score = vertical_O_score = 0
		diagonal_X_flag = diagonal_O_flag = diagonal_1_X_flag = diagonal_1_O_flag = 0
		diagonal_X_score = diagonal_O_score = diagonal_1_X_score = diagonal_1_O_score = 0

		#Possible Horizontal Wins
		for i in range(self.gp.size_of_board):
			for j in range(self.gp.size_of_board):
				if (j <= self.gp.size_of_board - self.gp.line_up_size):
					for k in range(self.gp.line_up_size):
						if (self.current_state[i][j+k] == 'X' or self.current_state[i][j+k] == '.'):
							horizontal_X_flag += 1
						elif (self.current_state[i][j+k] == 'O' or self.current_state[i][j+k] == '.'):
							horizontal_O_flag += 1
					self.nb_of_evaluated_states += 1
					if (self.gp.line_up_size == horizontal_X_flag):
						horizontal_X_score += 1
					elif (self.gp.line_up_size == horizontal_O_flag):
						horizontal_O_score += 1
					horizontal_X_flag = horizontal_O_flag = 0
		horizontal_score = horizontal_O_score - horizontal_X_score

		#Possible Vertical Wins
		for i in range(self.gp.size_of_board):
			for j in range(self.gp.size_of_board):
				if (i <= self.gp.size_of_board - self.gp.line_up_size):
					for k in range(self.gp.line_up_size):
						if (self.current_state[i+k][j] == 'X' or self.current_state[i+k][j] == '.'):
							vertical_X_flag += 1
						elif (self.current_state[i+k][j] == 'O' or self.current_state[i+k][j] == '.'):
							vertical_O_flag += 1
					self.nb_of_evaluated_states += 1
					if (self.gp.line_up_size == vertical_X_flag):
						vertical_X_score += 1
					elif (self.gp.line_up_size == vertical_O_flag):
						vertical_O_score += 1
					vertical_X_flag = vertical_O_flag = 0
		vertical_score = vertical_O_score - vertical_X_score

		# Diagonal win
		for i in range(self.gp.size_of_board):
			for j in range(self.gp.size_of_board):
				if (i <= self.gp.size_of_board - self.gp.line_up_size and j <= self.gp.size_of_board - self.gp.line_up_size):
					for k in range(self.gp.line_up_size):
						if (self.current_state[i+k][j+k] == 'X' or self.current_state[i+k][j+k] == '.'):
							diagonal_X_flag += 1
						elif (self.current_state[i+k][j+k] == 'O' or self.current_state[i+k][j+k] == '.'):
							diagonal_O_flag += 1
					self.nb_of_evaluated_states += 1
					if diagonal_X_flag == self.gp.line_up_size:
						diagonal_X_score += 1
					elif diagonal_O_flag == self.gp.line_up_size:
						diagonal_O_score += 1
					diagonal_X_flag = diagonal_O_flag = 0
				
				if (i <= self.gp.size_of_board - self.gp.line_up_size and j >= self.gp.line_up_size -1):
					for k in range(self.gp.line_up_size):
						if (self.current_state[i+k][j-k] == 'X' or self.current_state[i+k][j-k] == '.'):
							diagonal_1_X_flag += 1
						elif (self.current_state[i+k][j-k] == 'O' or self.current_state[i+k][j-k] == '.'):
							diagonal_1_O_flag += 1
					self.nb_of_evaluated_states += 1
					if diagonal_1_X_flag == self.gp.line_up_size:
						diagonal_1_X_score += 1
					elif diagonal_1_O_flag == self.gp.line_up_size:
						diagonal_1_O_score += 1
					diagonal_1_X_flag = diagonal_1_O_flag = 0
		diagonal_score = (diagonal_O_score + diagonal_1_O_score) - (diagonal_X_score + diagonal_1_X_score)
		# win_paths_for_O - win_paths_for_X
		score = horizontal_score + vertical_score + diagonal_score
		return score


	#Didn't touch this yet
	def minimax(self, max=False):
		# Minimizing for 'X' and maximizing for 'O'
		# Possible values are:
		# -1 - win for 'X'
		# 0  - a tie
		# 1  - loss for 'X'
		# We're initially setting it to 2 or -2 as worse than the worst case:
		if self.player_turn == 'O':
			depth_limit = self.d2
		else:
			depth_limit = self.d1

		x = y = None
		end = time.time()
		if max and (end - self.start) > self.gp.threshold:
			print(self.current_depth)
			return (-1, None, None)
		elif max==False and (end - self.start) > self.gp.threshold:
			print(self.current_depth)
			return (1, None, None)
		
		value = 100000
		if max:
			value = -100000

		self.current_depth += 1

		end_check = self.is_end()
		if end_check == 'X':
			self.current_depth = 0
			return (-99999, x, y)
		elif end_check == 'O':
			self.current_depth = 0
			return (99999, x, y)
		elif end_check == '.':
			self.current_depth = 0
			return (0, x, y)

		# check for the self.current_depth
		if self.current_depth > depth_limit:
			self.current_depth -= 1
			result = self.possible_win_paths()
			return (result, x, y)

		for i in range(self.gp.size_of_board):
			for j in range(self.gp.size_of_board):
				if self.current_state[i][j] == '.':
					if max and self.current_depth <= depth_limit:
						self.current_state[i][j] = 'O'
						(v, _, _) = self.minimax(max=False)
						if v > value:
							value = v
							x = i
							y = j
					elif max is False and self.current_depth <= depth_limit:
						self.current_state[i][j] = 'X'
						(v, _, _) = self.minimax(max=True)
						if v < value:
							value = v
							x = i
							y = j
					self.current_state[i][j] = '.'

		return (value, x, y)

	def alphabeta(self, alpha=-2, beta=2, max=False):
		# Minimizing for 'X' and maximizing for 'O'
		# Possible values are:
		# -1 - win for 'X'
		# 0  - a tie
		# 1  - loss for 'X'
		# We're initially setting it to 2 or -2 as worse than the worst case:
		end = time.time()
		if max and (end - self.start) > self.gp.threshold:
			return (-1, None, None)
		elif max == False and (end - self.start) > self.gp.threshold:
			return (1, None, None)

		value = 2
		if max:
			value = -2
		x = None
		y = None
		result = self.is_end()
		if result == 'X':
			return (-1, x, y)
		elif result == 'O':
			return (1, x, y)
		elif result == '.':
			return (0, x, y)
		for i in range(0, 3):
			for j in range(0, 3):
				if self.current_state[i][j] == '.':
					if max:
						self.current_state[i][j] = 'O'
						(v, _, _) = self.alphabeta(alpha, beta, max=False)
						if v > value:
							value = v
							x = i
							y = j
					else:
						self.current_state[i][j] = 'X'
						(v, _, _) = self.alphabeta(alpha, beta, max=True)
						if v < value:
							value = v
							x = i
							y = j
					self.current_state[i][j] = '.'
					if max:
						if value >= beta:
							return (value, x, y)
						if value > alpha:
							alpha = value
					else:
						if value <= alpha:
							return (value, x, y)
						if value < beta:
							beta = value
		return (value, x, y)

	def play(self):
		list_of_chars = [string.ascii_uppercase[i] for i in range(self.gp.size_of_board)]
		while True:
			file_name = "gameTrace-" + str(self.gp.size_of_board) + str(len(self.gp.blocs_coordinates)) + str(self.gp.line_up_size) + str(self.gp.threshold) + '.txt'
			with open(file_name , "a") as myfile:
				myfile.write(self.draw_board() + '\n\n')
			print(self.draw_board())
			if self.check_end():
				return
			self.start = time.time()
			self.nb_of_evaluated_states = 0 
			self.current_depth = 0
			if self.gp.minimax_alphabeta_bool == self.MINIMAX:
				if self.player_turn == 'X':
					(_, x, y) = self.minimax(max=False)
				else:
					(_, x, y) = self.minimax(max=True)
			else: # algo == self.ALPHABETA
				if self.player_turn == 'X':
					(m, x, y) = self.alphabeta(max=False)
				else:
					(m, x, y) = self.alphabeta(max=True)
			end = time.time()
			if (self.player_turn == 'X' and self.mode_of_play()[0] == self.HUMAN) or (self.player_turn == 'O' and self.mode_of_play()[1] == self.HUMAN):
					if self.recommend:
						with open(file_name, "a") as myfile:
							myfile.write(F'\nEvaluation time: {round(end - self.start, 7)}s')
							myfile.write(F'\nRecommended move: x = {x}, y = {list_of_chars[y]}')
						print(F'Evaluation time: {round(end - self.start, 7)}s')
						print(F'Recommended move: x = {x}, y = {list_of_chars[y]}')
					(x,y) = self.input_move()
			if (self.player_turn == 'X' and self.mode_of_play()[0] == self.AI) or (self.player_turn == 'O' and self.mode_of_play()[1] == self.AI):
						with open(file_name, "a") as myfile:
							myfile.write(F'Player {self.player_turn} under AI control plays: x = {x}, y = {list_of_chars[y]}\n\n')
							myfile.write(F'\ni\tEvaluation time: {round(end - self.start, 7)}s\n')
							myfile.write(F'\nii\tHeuristic evaluations: {self.nb_of_evaluated_states}\n')
						print(F'Evaluation time: {round(end - self.start, 7)}s')
						print(F'Player {self.player_turn} under AI control plays: x = {x}, y = {list_of_chars[y]}')
			self.current_state[x][y] = self.player_turn
			self.switch_player()

