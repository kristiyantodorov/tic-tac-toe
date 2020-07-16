import time

from game import Game
from node import Node
from tree import Tree

BOARD_SIZE = 3

if __name__ == '__main__':
    ai_ai_mode = "AI vs AI"
    ai_human_mode = "AI vs human"
    game = Game(ai_human_mode, BOARD_SIZE)