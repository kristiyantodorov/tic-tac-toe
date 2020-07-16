
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
    def __init__(self, state, player, board_size):
        self.state = state
        self.player = player
        self.utility = 0
        self.children = [None, None, None, None, None, None, None, None, None]
        self.alpha = float('-inf')
        self.beta = float('inf')
        self.board_size = board_size

    def winning_state(self):
        for st in WINNING_STATES:
            first, second, third = st[0], st[1], st[2]
            if self.state[first] == self.state[second] == self.state[third]  != ' ':
                return_value = 1 if self.state[first] == 'X' else -1
                return return_value

        return 0

    def available_moves(self):
        available_moves = []
        for i in range(0, self.board_size * self.board_size):
            if self.state[i] == ' ':
                available_moves.append(i)

        return available_moves