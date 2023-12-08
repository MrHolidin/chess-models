from chess import Board
import random
from Player import Player

class RandomPlayer(Player):
    def get_next_move(self, board: Board):
        moves = list(board.legal_moves)
        return random.choice(moves)