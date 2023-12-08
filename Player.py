from chess import Board, Move
from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def get_next_move(self, board: Board) -> Move:
        pass