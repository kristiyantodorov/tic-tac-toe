import time

from tree import Tree
from node import Node

class Game():
    def __init__(self, mode, board_size):
        self.board_size = board_size
        player = 'X'
        state = [' ', ' ', ' ',
                 ' ', ' ', ' ',
                 ' ', ' ', ' ']
        root = Node(state, player, board_size)

        print("AI learning stage")
        Tree(root, board_size)

        self.root = root
        self.game_mode = mode
        self.game_loop(root)

    def game_loop(self, node):
        self.node = self.root
        while(True):
            print("######################################\nStarting new game\n######################################")
            while self.node.winning_state() == 0:
                self.ai_turn(1)
                if self.node.winning_state() == 1:
                    self.print_winning('ai')
                    break
                elif self.node.available_moves() == []:
                    self.print_winning('tie')
                    break

                self.print_table(self.node.state)

                if self.game_mode == "AI vs AI":
                    self.ai_turn(-1)
                    time.sleep(1)
                    if self.node.winning_state() == 1:
                        self.print_winning('ai')
                        break
                    elif self.node.available_moves() == []:
                        self.print_winning('tie')
                        break
                elif self.game_mode == "AI vs human":
                    self.human_turn()
                    if self.node.winning_state() == -1:
                        self.print_winning('human')
                        break

    def print_winning(self, player):
        print('---------------------')
        if player == 'human':
            print("!!! The human won !!!")
        elif player == 'ai':
            print("!!! The AI won !!!")
        elif player == 'tie':
            print("!!! It's a tie !!!")
        print('---------------------')
        self.print_table(self.node.state)
        self.node = self.root


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
        x, y = [int(x) for x in input("Enter position: ").split(' ')]
        position = x*self.board_size + y

        while position > 8 or position < 0 or self.node.state[position] != ' ':
            print("Wrong position! Choose another one:\n")
            x, y = [int(x) for x in input("Enter position: ").split(' ')]
            position = x*self.board_size + y

        self.node = self.node.children[position]
        return

    def print_table(self, state):
        print('-------------')

        for i in range(0, self.board_size):
            print('|', end=' ')
            for j in range(0, self.board_size):
                print(state[i*self.board_size+j], '|', end=' '),
            print('\n-------------')
