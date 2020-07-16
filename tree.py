
import copy

from node import Node

class Tree():
    def __init__(self, root_node, board_size):
        self.board_size = board_size
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
            
            new_node = Node(new_state, new_player, self.board_size)
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
