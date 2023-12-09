from chess import Board, Move
import random
from Player import Player

class RandomPlayer(Player):
    def get_next_move(self, board: Board) -> Move:
        moves = list(board.legal_moves)
        return random.choice(moves)