from Player import Player
from chess import Board, Move
from PositionEstimators import PositionEstimator
import typing as tp


class BriethSearchPlayer(Player):
    def __init__(self, estimator: PositionEstimator, depth: int = 4):
        if depth <= 0:
            raise ValueError("Deep for BriethSearchPlayer can't be lower than 0")
        self.depth = depth
        self.estimator = estimator

    def _best_value_with_move(self, board: Board, depth: int) -> tp.Tuple[float, Move]:
        if depth == 0:
            return self.estimator(board), Move.null()
        best_move = Move.null()
        best_res = -1e9
        for move in board.legal_moves:
            board.push(move)
            res, _ = self._best_value_with_move(board, depth - 1)
            board.pop()
            res = -res
            if res > best_res:
                best_res = res
                best_move = move
        return best_res, best_move

    def get_next_move(self, board) -> Move:
        _, move = self._best_value_with_move(board, self.depth)
        assert move
        return move
