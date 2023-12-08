import chess
from chess import Board
from abc import ABC, abstractmethod
import typing as tp


class PositionEstimator(ABC):
    @abstractmethod
    def __call__(self, board: Board) -> float:
        pass


def SimpleEstimator(PositionEstimator):
    pieces_values: tp.Dict[int, float] = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 100,
    }

    def __call__(self, board: Board) -> float:
        if board.is_checkmate():
            return -1000
        estimation = 0
        for piece in board.piece_map().values():
            estimation += (
                pieces_values[piece.piece_type]
                * (1 if piece.color == chess.WHITE else -1)
                * (1 if board.turn == chess.WHITE else -1)
            )
        estimation += len(list(board.legal_moves)) * 1e-2
        return estimation
