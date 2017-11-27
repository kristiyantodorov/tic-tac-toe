import time
import copy

BOARD_SIZE = 3
WINNING_STATES = [
        # Horizontal
        [0,1,2],
        [3,4,5],
        [6,7,8],
        # Vertical
        [0,3,6],
        [1,4,7],
        [2,5,8],
        # Diagonal
        [0,4,8],
        [2,4,6]
        ]

class Node():
	def __init__(self, state, player):
		self.state = state
		self.player = player
		self.utility = 0
		self.children = [None, None, None, None, None, None, None, None, None]
		self.alpha = float('-inf')
		self.beta = float('inf')

	def winning_state(self):
		for st in WINNING_STATES:
			first, second, third = st[0], st[1], st[2]
			if self.state[first] == self.state[second] == self.state[third]  != ' ':
				return_value = 1 if self.state[first] == 'X' else -1
				return return_value

		return 0

	def available_moves(self):
		available_moves = []
		for i in range(0, BOARD_SIZE*BOARD_SIZE):
			if self.state[i] == ' ':
				available_moves.append(i)

		return available_moves

class Tree():
	def __init__(self, root_node):
		self.root = root_node
		self.generate_tree(self.root)
		self.alpha = float('-inf')
		self.beta = float('inf')

	def generate_tree(self, node):

		for i in node.available_moves():
			utility = node.winning_state()
			if utility != 0:
				node.utility = 1 if utility == 1 else -1
				break

			new_state = copy.deepcopy(node.state)
			new_state[i] = node.player

			new_player = 'O' if node.player == 'X' else 'X'
			
			new_node = Node(new_state, new_player)
			node.children[i] = new_node
			self.generate_tree(node.children[i])

		try:
			if node.player == 'X':
				node.utility = max(n.utility for n in node.children if n != None)
				node.alpha = max(n.utility for n in node.children if n != None)
			else:
				node.utility = min(n.utility for n in node.children if n != None)
		except ValueError:
				pass


def print_table(state):
	print '-------------'

	for i in range(0, BOARD_SIZE):
		print '|',
		for j in range(0, BOARD_SIZE):
			print state[i*BOARD_SIZE+j], '|',
		print '\n-------------'

class Game():
	def __init__(self, root, mode):
		self.root = root
		self.game_mode = mode
		self.game_loop(root)

	def game_loop(self, node):
		self.node = self.root
		while(True):
			print "######################################\nStarting new game\n######################################"
			while self.node.winning_state() == 0:
				self.ai_turn(1)
				if self.node.winning_state() == 1:
					print '------------------'
					print "!!! The AI won !!!"
					print '------------------'
					print_table(self.node.state)
					self.node = self.root
					break
				elif self.node.available_moves() == []:
					print '------------------'
					print "!!! It's a tie !!!"
					print '------------------'					
					print_table(self.node.state)
					self.node = self.root
					break

				print_table(self.node.state)

				if self.game_mode == "AI vs AI":
					self.ai_turn(-1)
					time.sleep(1)
					if self.node.winning_state() == 1:
						print '------------------'
						print "!!! The AI won !!!"
						print '------------------'
						print_table(self.node.state)
						self.node = self.root
						break
					elif self.node.available_moves() == []:
						print '------------------'
						print "!!! It's a tie !!!"
						print '------------------'					
						print_table(self.node.state)
						self.node = self.root
						break
				elif self.game_mode == "AI vs human":
					self.human_turn()
					if self.node.winning_state() == -1:
						print '---------------------'
						print "!!! The human won !!!"
						print '---------------------'
						print_table(self.node.state)
						self.node = self.root
						break

	def ai_turn(self, goal):
		max_util = -2 if goal == 1 else 2
		chosen_node = None
		for n in self.node.children:
			if n != None:
				if goal == 1:
					if n.utility >= max_util:
						max_util = n.utility
						chosen_node = n
				else:
					if n.utility <= max_util:
						max_util = n.utility
						chosen_node = n

		self.node = chosen_node

	def human_turn(self):
		x, y = [int(x) for x in raw_input("Enter position: ").split(' ')]
		position = x*BOARD_SIZE + y

		while position > 8 or position < 0 or self.node.state[position] != ' ':
			print "Wrong position! Choose another one:\n"
			x, y = [int(x) for x in raw_input("Enter position: ").split(' ')]
			position = x*BOARD_SIZE + y

		self.node = self.node.children[position]
		return

if __name__ == '__main__':
	player = 'X'
	state = [' ', ' ', ' ',
			 ' ', ' ', ' ',
			 ' ', ' ', ' ']
	node = Node(state, 'X')
	tree = Tree(node)
	ai_ai_mode = "AI vs AI"
	ai_human_mode = "AI vs human"
	game = Game(node, ai_ai_mode)